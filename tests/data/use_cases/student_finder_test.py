from src.data.use_cases.student_finder import StudentFinder 
from src.domain.models.students import Students
from tests.db.repositories.students_repository_test import StudentsRepositorySpy

def test_find():
    search = 'test'
    
    repository = StudentsRepositorySpy()
    student_finder = StudentFinder(repository)
    
    response = student_finder.find(search)
    
    
    assert repository.select_student_attributes['search'] == search
    
    assert response['type'] == 'Students'
    assert response['count'] == len(response['data'])
    assert response['data'] != []

def test_find_error_user_not_found():
    class StudentsRepositoryError(StudentsRepositorySpy):
        def select_student(self, search: str = '') -> list[Students]:
            return []
    
    search = 'test'
    
    repository = StudentsRepositoryError()
    student_finder = StudentFinder(repository)
    
    try:
        student_finder.find(search)
        assert False
    except Exception as exception:
        assert str(exception) == "No students found with the given search term"