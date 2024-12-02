from fastapi import APIRouter, Query, Depends
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.student_finder_composer import student_finder_composer
from src.main.composers.student_register_composer import student_register_composer
from src.main.composers.student_finder_by_id_composer import student_finder_by_id_composer
from src.main.composers.student_delete_composer import student_delete_composer
from src.main.composers.student_update_composer import student_updater_composer
from src.presentation.schemas.student_search_schema import StudentSearchSchema, StudentInputSchema, StudentEmailSchema
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

@router.get('/students/{id}')
async def find_student_by_id(id: int):
    http_request = HttpRequest(path_params={"id":id})
    http_response = await request_adapter(http_request, student_finder_by_id_composer())
    return http_response.body

@router.delete('/students/{id}')
async def delete_student(id: int):
    http_request = HttpRequest(path_params={"id":id})
    http_response = await request_adapter(http_request, student_delete_composer())
    return http_response.body

@router.patch('/students/{id}')
async def update_student(id: int, email: StudentEmailSchema):
    http_request = HttpRequest(body={"id": id,"email": email.email})
    http_response = await request_adapter(http_request, student_updater_composer())
    return http_response.body
    