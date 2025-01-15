from sqlalchemy.orm import Session
from app.models import Record


def create_record(db: Session, record_data: dict):
    record = Record(**record_data)
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def get_record_by_id(db: Session, record_id: str):
    return db.query(Record).filter(Record.id == record_id).first()


def update_record_status(db: Session, record_id: str, status: str):
    record = get_record_by_id(db, record_id)
    if record:
        record.status = status
        db.commit()
        db.refresh(record)
        return record
    return None
