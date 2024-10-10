from src.domain.use_cases.student_register import StudentRegister as StudentRegisterInterface
from src.data.interfaces.student_repository import StudentsRepositoryInterface
from src.errors.types.http_conflict import HttpConflictError

class StudentRegister(StudentRegisterInterface):
    def __init__(self, students_repository: StudentsRepositoryInterface) -> None:
        self.__student_repository = students_repository
    
    def register(self, name: str, email: str) -> dict:
        existing_student = self.__student_repository.select_student(email)
        if existing_student:
            raise HttpConflictError("Email already exists.")
        self.__student_repository.insert_student(name, email)
        
        response = {
            "type": "Students",
            "students": {
                "name": name,
                "email": email
            }
            
        }
        
        return response
        
    