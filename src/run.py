from fastapi import FastAPI
from src.config import configure_app

app = FastAPI()

configure_app(app)

@app.get('/health-check')
def health_check():
    return {"healthy": True}
