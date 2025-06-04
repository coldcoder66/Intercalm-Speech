from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import get_db

router = APIRouter()

# In-memory database for lessons
lessons_db = []

class Lesson(BaseModel):
    id: int
    title: str
    description: Optional[str] = None

@router.get("/test-db")
def test_database_connection(db: Session = Depends(get_db)):
    """Test endpoint to verify database connectivity"""
    try:
        result = db.execute(text("SELECT 1 as test"))
        return {"status": "success", "message": "Database connection working"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@router.post("/", response_model=Lesson)
def create_lesson(lesson: Lesson):
    lessons_db.append(lesson)
    return lesson

@router.get("/{lesson_id}", response_model=Lesson)
def get_lesson(lesson_id: int):
    for lesson in lessons_db:
        if lesson.id == lesson_id:
            return lesson
    raise HTTPException(status_code=404, detail="Lesson not found")

@router.put("/{lesson_id}", response_model=Lesson)
def update_lesson(lesson_id: int, updated_lesson: Lesson):
    for i, lesson in enumerate(lessons_db):
        if lesson.id == lesson_id:
            lessons_db[i] = updated_lesson
            return updated_lesson
    raise HTTPException(status_code=404, detail="Lesson not found")

@router.delete("/{lesson_id}")
def delete_lesson(lesson_id: int):
    global lessons_db
    lessons_db = [lesson for lesson in lessons_db if lesson.id != lesson_id]
    return {"message": "Lesson deleted"}
