from fastapi import FastAPI
from src.errors.error_handler import handle_errors
from src.main.routes.routes import router as student_routes

def configure_app(app: FastAPI):
    handle_errors(app)
    
    app.include_router(student_routes)