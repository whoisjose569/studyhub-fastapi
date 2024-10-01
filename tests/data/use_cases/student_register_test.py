from src.data.use_cases.student_register import StudentRegister
from tests.db.repositories.students_repository_test import StudentsRepositorySpy

def test_register():
    name = 'test'
    email = 'test@email'
    
    repository = StudentsRepositorySpy()
    student_register = StudentRegister(repository)
    
    response = student_register.register(name, email)
    
    assert repository.insert_student_attributes["name"] == name
    assert repository.insert_student_attributes["email"] == email
    
    assert response['type'] == 'Students'
    assert response['data'] != []