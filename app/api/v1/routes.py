from fastapi import APIRouter
from app.schema.note import Note

router = APIRouter()

# in-memory db (a simple list)
notes_db = []

@router.post("/notes")
async def create_note(note: Note):
    notes_db.append(note)
    return {"message": "Note created successfully", "note": note}

@router.get("/notes")
async def get_notes():
    return notes_db

@router.get("/hello")
async def say_hello():
    return {"message": "Hello from v1 routes!"}