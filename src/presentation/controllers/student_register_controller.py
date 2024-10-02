from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.student_register import StudentRegister as StudentRegisterInterface

class StudentRegisterController(ControllerInterface):
    def __init__(self, use_case: StudentRegisterInterface) -> None:
        self.__use_case = use_case
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        name = http_request.body["name"]
        email = http_request.body["email"]
        
        response = self.__use_case.register(name, email)
        
        return HttpResponse(
            status_code=200,
            body={"data": response}
        )