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

# Додавання CORS middleware для дозволу запитів з фронтенду
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Дозволяємо запити з будь-якого джерела
    allow_credentials=True,
    allow_methods=["*"],  # Дозволяємо всі методи
    allow_headers=["*"],  # Дозволяємо всі заголовки
)


# Обробка POST запиту для генерації тексту
@app.post("/generate/", response_model=RecordResponse)
async def generate_text(file: UploadFile = File(...), text: str = Form(...), db: Session = Depends(get_db)):
    record_id = str(uuid.uuid4())
    file_name = f"{record_id}.txt"

    try:
        # Завантаження файлу до S3
        s3_link = upload_to_s3(file.file, file_name)  # Файл передається як file.file
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # Створення запису в базі даних
    record_data = {
        "id": record_id,
        "link": s3_link,
        "status": "processing",
        "text": text  # Використовуємо текст, що переданий в формі
    }
    record = create_record(db, record_data)

    # Виклик асинхронного процесу для подальшої обробки
    process_record.delay(record_id)

    return record  # Record буде автоматично перетворено в RecordResponse


# Отримання запису за ID
@app.get("/records/{record_id}", response_model=RecordResponse)
async def read_record(record_id: str, db: Session = Depends(get_db)):
    record = get_record_by_id(db, record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    return record  # Record буде автоматично перетворено в RecordResponse


# Перевірка здоров'я сервера
@app.get("/api/health")
async def health_check():
    return {"status": "ok"}
