from src.domain.use_cases.students_use_cases.student_delete import StudentDelete as StudentDeleteInterface
from src.data.interfaces.student_repository import StudentsRepositoryInterface
from src.errors.types import HttpNotFoundError

class StudentDelete(StudentDeleteInterface):
    def __init__(self, students_repository: StudentsRepositoryInterface) -> None:
        self.__students_repository = students_repository
    
    def delete(self, id: int) -> dict:
        student = self.__students_repository.select_student_by_id(id)
        if student is None:
            raise HttpNotFoundError("No students found with the given id")
        
        self.__students_repository.delete_student(id)
        
        response = {
            "message": "Student successfully deleted",
        }
        return response