from src.infra.db.repositories.students_repository import StudentsRepository
from src.data.use_cases.student_finder_by_id import StudentFinderById
from src.presentation.controllers.student_controllers.student_finder_by_id_controller import StudentFinderByIdController

def student_finder_by_id_composer():
    repository = StudentsRepository()
    use_case = StudentFinderById(repository)
    controller = StudentFinderByIdController(use_case)
    
    return controller.handle