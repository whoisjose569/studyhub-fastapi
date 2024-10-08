from src.infra.db.repositories.students_repository import StudentsRepository
from src.data.use_cases.student_register import StudentRegister
from src.presentation.controllers.student_register_controller import StudentRegisterController

def student_register_composer():
    repository = StudentsRepository()
    use_case = StudentRegister(repository)
    controller = StudentRegisterController(use_case)
    
    return controller.handle