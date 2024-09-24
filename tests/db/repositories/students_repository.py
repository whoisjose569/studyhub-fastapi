from src.domain.models.students import Students


class StudentsRepositorySpy:
    def __init__(self) -> None:
        self.insert_student_attributes = {}
        self.select_student_attributes = {}
    
    def insert_student(self, name: str, email: str) -> None:
        self.insert_student_attributes["name"] = name
        self.insert_student_attributes["email"] = email
        return
    
    def select_student(self, search: str = '') -> list[Students]:
        self.select_student_attributes['search'] = search
        return [
            Students(1,search,'test@test','2024-10-15'),
            Students(2,search,'jove@test','2024-01-02')
        ]