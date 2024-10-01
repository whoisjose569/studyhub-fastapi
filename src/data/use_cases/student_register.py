from src.domain.use_cases.student_register import StudentRegister as StudentRegisterInterface
from src.data.interfaces.student_repository import StudentsRepositoryInterface


class StudentRegister(StudentRegisterInterface):
    def __init__(self, students_repository: StudentsRepositoryInterface) -> None:
        self.__student_repository = students_repository
    
    def register(self, name: str, email: str) -> dict:
        self.__student_repository.insert_student(name, email)
        
        response = {
            "type": "Students",
            "data": {
                "name": name,
                "email": email
            }
            
        }
        
        return response
        
    