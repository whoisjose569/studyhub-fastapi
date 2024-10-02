from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.student_finder import StudentFinder as StudentFinderInterface

class StudentFinderController(ControllerInterface):
    def __init__(self, use_case: StudentFinderInterface) -> None:
        self.__use_case = use_case
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        search = http_request.query_params["search"]
        
        response = self.__use_case.find(search)
        
        return HttpResponse(
            status_code=200,
            body={"data": response}
        )