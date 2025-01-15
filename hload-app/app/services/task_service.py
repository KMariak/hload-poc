# app/services/task_service.py
from app.celery_app import celery_app
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import update_record_status
import time


@celery_app.task
def process_record(record_id: str):
    time.sleep(10)  # Симуляція тривалої операції

    db: Session = SessionLocal()
    update_record_status(db, record_id, "done")
    db.close()
