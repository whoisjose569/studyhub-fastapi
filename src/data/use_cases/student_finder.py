from src.domain.use_cases.students_finder import StudentFinder as StudentFinderInterface
from src.data.interfaces.student_repository import StudentsRepositoryInterface

class StudentFinder(StudentFinderInterface):
    def __init__(self, students_repository: StudentsRepositoryInterface) -> None:
        self.__students_repository = students_repository
    
    def find(self, search: str) -> dict:
        pass