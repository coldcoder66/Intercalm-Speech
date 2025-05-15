from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

# In-memory database for quizzes
quizzes_db = []

class Quiz(BaseModel):
    id: int
    title: str
    description: Optional[str] = None

@router.post("/", response_model=Quiz)
def create_quiz(quiz: Quiz):
    quizzes_db.append(quiz)
    return quiz

@router.get("/{quiz_id}", response_model=Quiz)
def get_quiz(quiz_id: int):
    for quiz in quizzes_db:
        if quiz.id == quiz_id:
            return quiz
    raise HTTPException(status_code=404, detail="Quiz not found")

@router.put("/{quiz_id}", response_model=Quiz)
def update_quiz(quiz_id: int, updated_quiz: Quiz):
    for i, quiz in enumerate(quizzes_db):
        if quiz.id == quiz_id:
            quizzes_db[i] = updated_quiz
            return updated_quiz
    raise HTTPException(status_code=404, detail="Quiz not found")

@router.delete("/{quiz_id}")
def delete_quiz(quiz_id: int):
    global quizzes_db
    quizzes_db = [quiz for quiz in quizzes_db if quiz.id != quiz_id]
    return {"message": "Quiz deleted"}
