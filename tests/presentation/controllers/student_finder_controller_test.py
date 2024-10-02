from src.presentation.controllers.student_finder_controller import StudentFinderController
from tests.data.tests.student_finder import StudentFinderSpy
from src.presentation.http_types.http_response import HttpResponse

class HttpRequestMock():
    def __init__(self) -> None:
        self.query_params = {"search": "test"}

def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = StudentFinderSpy()
    student_finder_controller = StudentFinderController(use_case)
    
    response = student_finder_controller.handle(http_request_mock)
    
    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"] is not None