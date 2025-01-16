from sqlalchemy.orm import Session
from app.models import Record
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_record(db: Session, record_data: dict):
    logger.info(f"Creating a new record with data: {record_data}")
    record = Record(**record_data)
    db.add(record)
    db.commit()
    db.refresh(record)
    logger.info(f"Record created with ID: {record.id}")
    return record


def get_record_by_id(db: Session, record_id: str):
    logger.info(f"Fetching record with ID: {record_id}")
    record = db.query(Record).filter(Record.id == record_id).first()
    if record:
        logger.info(f"Record found: {record}")
    else:
        logger.warning(f"Record with ID {record_id} not found.")
    return record


def update_record_status(db: Session, record_id: str, status: str):
    logger.info(f"Updating status of record with ID: {record_id} to '{status}'")
    record = get_record_by_id(db, record_id)
    if record:
        record.status = status
        db.commit()
        db.refresh(record)
        logger.info(f"Record with ID {record_id} updated to status '{status}'")
        return record
    else:
        logger.warning(f"Record with ID {record_id} not found. Status update failed.")
    return None
