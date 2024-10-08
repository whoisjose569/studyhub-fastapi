from fastapi import APIRouter, Query, Depends
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.student_finder_composer import student_finder_composer
from src.main.composers.student_register_composer import student_register_composer
from src.presentation.schemas.student_search_schema import StudentSearchSchema, StudentInputSchema
from src.presentation.http_types.http_request import HttpRequest

router = APIRouter()

@router.get('/students')
async def find_student(search: StudentSearchSchema = Depends()):
    http_request = HttpRequest(query_params=search.dict())
    http_response = await request_adapter(http_request, student_finder_composer())
    return http_response.body

@router.post('/students')
async def register_student(student: StudentInputSchema):
    http_request = HttpRequest(body=student.dict())
    http_response = await request_adapter(http_request, student_register_composer())
    return http_response.body