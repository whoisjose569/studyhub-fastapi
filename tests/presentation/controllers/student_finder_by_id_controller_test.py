from src.presentation.controllers.student_finder_by_id_controller import StudentFinderByIdController
from tests.data.tests.student_finder_by_id_test import StudentFinderByIdSpy
from src.presentation.http_types.http_response import HttpResponse

class HttpRequestMock():
    def __init__(self) -> None:
        self.path_params = {"id": 1}

def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = StudentFinderByIdSpy()
    student_finder_controller = StudentFinderByIdController(use_case)
    
    response = student_finder_controller.handle(http_request_mock)
    
    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"] is not None