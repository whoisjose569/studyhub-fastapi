from fastapi import FastAPI
from src.main.routes.routes import router as student_routes
from src.errors.error_handler import handle_errors

app = FastAPI()
handle_errors(app)


@app.get('/health-check')
def health_check():
    return {"healthy": True}

app.include_router(student_routes)
