from src.domain.use_cases.student_update import StudentUpdater as StudentUpdaterInterface
from src.data.interfaces.student_repository import StudentsRepositoryInterface
from src.errors.types.http_conflict import HttpConflictError

class StudentUpdater(StudentUpdaterInterface):
    def __init__(self, students_repository: StudentsRepositoryInterface) -> None:
        self.__student_repository = students_repository
    
    def update(self, id: int, email: str) -> dict:
        existing_student = self.__student_repository.select_student_by_id(id)
        if not existing_student:
            raise HttpConflictError("Student not found.")
        
        if self.__student_repository.select_student(email):
            raise HttpConflictError("Email already in use.")
        
        self.__student_repository.update_student(id, email)
        
        response = {
            "message": "Student email successfully updated",
            "new email": email 
        }
        
        return response