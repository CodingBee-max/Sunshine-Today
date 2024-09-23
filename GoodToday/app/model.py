from pydantic import BaseModel
from typing import Optional


class NoteRequest(BaseModel):
    title: Optional[str]
    content: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "request_id": "1234-04x4-894",
                "title": "Great Day",
                "content": "Went to the play den"
            }
        }


class NoteResponse(BaseModel):
    status_code: Optional[int]
    message: Optional[str]
    title: Optional[str]
    content: Optional[str]
