from pydantic import BaseModel, Field
from typing import Optional

class Note(BaseModel):
    id: int = Field(..., description="Unique identifier for the note")
    title: str = Field(..., max_length=100, description="Title of the note")
    content: Optional[str] = Field(None, description="Content of the note")

