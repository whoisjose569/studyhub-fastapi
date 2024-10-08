from fastapi import FastAPI
from src.main.routes.routes import router as student_routes
app = FastAPI()

@app.get('/health-check')
def health_check():
    return {"healthy": True}

app.include_router(student_routes)
