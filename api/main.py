import uvicorn
from fastapi import FastAPI
from routers import lessons, quizzes

app = FastAPI(title="Intercalm Speech API")

#Include routers
app.include_router(lessons.router, prefix="/lessons", tags=["Lessons"])
app.include_router(quizzes.router, prefix="/quizzes", tags=["Quizzes"])

@app.get("/")
def root():
    return {"message": "Welcome to the Intercalm Speech API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)