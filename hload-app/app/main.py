from fastapi import FastAPI
from pydantic import BaseModel
import boto3
from app.celery_app import add

app = FastAPI()

# Підключення до LocalStack S3
s3 = boto3.client(
    's3',
    endpoint_url='http://localstack:4566',  # Використовуємо LocalStack
    aws_access_key_id='test',
    aws_secret_access_key='test'
)

BUCKET_NAME = "hload-bucket"


class FileUpload(BaseModel):
    file_name: str
    file_content: str

# Маршрут для завантаження файлів у S3
@app.post("/upload/")
async def upload_file(file: FileUpload):
    s3.put_object(Bucket=BUCKET_NAME, Key=file.file_name, Body=file.file_content)
    return {"message": f"Файл {file.file_name} завантажено в S3!"}


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/api/health")
async def health_check():
    return {"status": "ok"}


@app.get("/tasks/add")
def run_task(x: int, y: int):
    task = add.delay(x, y)
    return {"task_id": task.id, "status": "Task sent to Celery"}
