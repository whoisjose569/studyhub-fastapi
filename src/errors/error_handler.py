from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from .types import HttpNotFoundError, HttpBadRequestError

def handle_errors(app: FastAPI):

    @app.exception_handler(HttpNotFoundError)
    async def not_found_handler(request: Request, exception: HttpNotFoundError):
        return JSONResponse(
            status_code=exception.status_code,
            content={
                "error": [{
                    "title": exception.name,
                    "detail": exception.message
                }]
            },
        )

    @app.exception_handler(HttpBadRequestError)
    async def bad_request_handler(request: Request, exception: HttpBadRequestError):
        return JSONResponse(
            status_code=exception.status_code,
            content={
                "error": [{
                    "title": exception.name,
                    "detail": exception.message
                }]
            },
        )

    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exception: Exception):
        return JSONResponse(
            status_code=500,
            content={
                "error": [{
                    "title": "Server Error",
                    "detail": str(exception)
                }]
            },
        )
