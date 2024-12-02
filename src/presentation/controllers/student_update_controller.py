from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.student_update import StudentUpdater as StudentUpdaterInterface

class StudentUpdateController(ControllerInterface):
    def __init__(self, use_case: StudentUpdaterInterface) -> None:
        self.__use_case = use_case
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        id = http_request.body["id"]
        email = http_request.body["email"]
        
        response = self.__use_case.update(id, email)
        
        return HttpResponse(
            status_code=200,
            body={"data": response}
        )