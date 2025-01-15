from app.database import SessionLocal
from app.crud import update_record_status
from celery import Celery
from sqlalchemy.orm import Session
import time


celery_app = Celery(
    'tasks',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0'
)


@celery_app.task
def process_record(record_id: str):
    time.sleep(10)

    db: Session = SessionLocal()
    update_record_status(db, record_id, "done")
    db.close()
