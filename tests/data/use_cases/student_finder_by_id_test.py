from src.data.use_cases.student_finder_by_id import StudentFinderById
from src.domain.models.students import Students
from tests.db.repositories.students_repository_test import StudentsRepositorySpy

def test_find_by_id():
    id = 1
    
    repository = StudentsRepositorySpy()
    student_finder = StudentFinderById(repository)
    
    response = student_finder.find_by_id(id)
    
    
    assert repository.select_student_attributes['id'] == id
    
    assert response['type'] == 'Students'
    assert response['students'] != []

def test_find_error_user_not_found():
    class StudentsRepositoryError(StudentsRepositorySpy):
        def select_student_by_id(self, id: int) -> Students:
            return []
    
    id = 1
    
    repository = StudentsRepositoryError()
    student_finder = StudentFinderById(repository)
    
    try:
        student_finder.find_by_id(id)
        assert False
    except Exception as exception:
        assert str(exception) == "No students found with the given id"