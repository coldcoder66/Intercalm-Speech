import uvicorn
import os
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from routers import lessons, quizzes, google_auth
from database import db_manager

app = FastAPI(title="Intercalm Speech API")
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

#Include routers
app.include_router(lessons.router, prefix="/lessons", tags=["Lessons"])
app.include_router(quizzes.router, prefix="/quizzes", tags=["Quizzes"])
app.include_router(google_auth.router, prefix="/google-auth", tags=["Auth"])

@app.get("/")
def root():
    return {"message": "Welcome to the Intercalm Speech API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)