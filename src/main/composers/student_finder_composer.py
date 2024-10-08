from src.infra.db.repositories.students_repository import StudentsRepository
from src.data.use_cases.student_finder import StudentFinder
from src.presentation.controllers.student_finder_controller import StudentFinderController

def student_finder_composer():
    repository = StudentsRepository()
    use_case = StudentFinder(repository)
    controller = StudentFinderController(use_case)
    
    return controller.handle