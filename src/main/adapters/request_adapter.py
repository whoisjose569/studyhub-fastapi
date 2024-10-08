from typing import Callable
from fastapi import Request as FastAPIRequest
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse

async def request_adapter(http_request: HttpRequest, controller: Callable) -> HttpResponse:
    http_response = controller(http_request)
    return http_response