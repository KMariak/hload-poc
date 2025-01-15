# app/schemas.py
from pydantic import BaseModel


class FileUpload(BaseModel):
    text: str

    class Config:
        orm_mode = True


class RecordResponse(BaseModel):
    id: str
    link: str
    text: str
    status: str

    class Config:
        orm_mode = True