from fastapi import FastAPI, Depends, HTTPException, File, Form, UploadFile
from sqlalchemy.orm import Session
from app.schemas import FileUpload, RecordResponse
from app.services.s3_service import upload_to_s3
from app.services.task_service import process_record
from app.database import Base, engine, get_db
from app.crud import create_record, get_record_by_id
from fastapi.middleware.cors import CORSMiddleware
import uuid

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/generate/", response_model=RecordResponse)
async def generate_text(file: UploadFile = File(...), text: str = Form(...), db: Session = Depends(get_db)):
    record_id = str(uuid.uuid4())
    file_name = f"{record_id}.txt"

    try:
        s3_link = upload_to_s3(file.file, file_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    record_data = {
        "id": record_id,
        "link": s3_link,
        "status": "processing",
        "text": text
    }
    record = create_record(db, record_data)

    process_record.delay(record_id)

    return record


@app.get("/records/{record_id}", response_model=RecordResponse)
async def read_record(record_id: str, db: Session = Depends(get_db)):
    record = get_record_by_id(db, record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    return record


@app.get("/api/health")
async def health_check():
    return {"status": "ok"}
