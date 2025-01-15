from sqlalchemy import Column, String
from app.database import Base


class Record(Base):
    __tablename__ = "records"

    id = Column(String, primary_key=True, index=True)
    link = Column(String, nullable=False)
    status = Column(String, default="processing")
    text = Column(String, nullable=False)
