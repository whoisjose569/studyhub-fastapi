from src.domain.use_cases.student_finder import StudentFinder as StudentFinderInterface
from src.data.interfaces.student_repository import StudentsRepositoryInterface
from src.errors.types import HttpNotFoundError

class StudentFinder(StudentFinderInterface):
    def __init__(self, students_repository: StudentsRepositoryInterface) -> None:
        self.__students_repository = students_repository
    
    def find(self, search: str) -> dict:
        students = self.__students_repository.select_student(search)
        if students == []:
            raise HttpNotFoundError("No students found with the given search term")
        
        response = {
            "type": "Students",
            "count": len(students),
            "students": [{
                "id": student.id,
                "name": student.name,
                "email": student.email,
                "enrollment_date": student.enrollment_date
            }
            for student in students
            ]
        }
        return response