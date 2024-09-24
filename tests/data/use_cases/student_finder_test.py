from src.data.use_cases.student_finder import StudentFinder 
from tests.db.repositories.students_repository import StudentsRepositorySpy

def test_find():
    search = 'test'
    
    repository = StudentsRepositorySpy()
    student_finder = StudentFinder(repository)
    
    response = student_finder.find(search)
    
    
    assert repository.select_student_attributes['search'] == search
    
    assert response['type'] == 'Students'
    assert response['count'] == len(response['data'])
    assert response['data'] != []