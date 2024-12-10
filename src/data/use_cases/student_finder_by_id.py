from src.domain.use_cases.students_use_cases.student_finder_by_id import StudentFinderById as StudentFinderByIdInterface
from src.data.interfaces.student_repository import StudentsRepositoryInterface
from src.errors.types import HttpNotFoundError

class StudentFinderById(StudentFinderByIdInterface):
    def __init__(self, students_repository: StudentsRepositoryInterface) -> None:
        self.__students_repository = students_repository
    
    def find_by_id(self, id: int) -> dict:
        student = self.__students_repository.select_student_by_id(id)
        if student is None:
            raise HttpNotFoundError("No students found with the given id")
        
        response = {
            "type": "Students",
            "students": {
                "id": student.id,
                "name": student.name,
                "email": student.email,
                "enrollment_date": student.enrollment_date
            }
        }
        return response