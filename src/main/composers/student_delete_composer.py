from src.infra.db.repositories.students_repository import StudentsRepository
from src.data.use_cases.student_delete import StudentDelete
from src.presentation.controllers.student_controllers.student_delete_controller import StudentDeleteController

def student_delete_composer():
    repository = StudentsRepository()
    use_case = StudentDelete(repository)
    controller = StudentDeleteController(use_case)
    
    return controller.handle