from src.infra.db.repositories.students_repository import StudentsRepository
from src.data.use_cases.student_update import StudentUpdater
from src.presentation.controllers.student_controllers.student_update_controller import StudentUpdateController

def student_updater_composer():
    repository = StudentsRepository()
    use_case = StudentUpdater(repository)
    controller = StudentUpdateController(use_case)
    
    return controller.handle