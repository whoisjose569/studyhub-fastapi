from abc import ABC, abstractmethod
from typing import Optional
from src.domain.models.students import Students

class StudentsRepositoryInterface(ABC):
    @abstractmethod
    def insert_student(self, name: str, email: str) -> None:
        pass
    
    @abstractmethod
    def select_student(self, search: str = '') -> list[Students]:
        pass
    
    @abstractmethod
    def select_student_by_id(self, id: int) -> Optional[Students]:
        pass
    
    @abstractmethod
    def delete_student(self, id: int) -> dict:
        pass
    
    @abstractmethod
    def update_student(self, id: int, email: str) -> Optional[Students]:
        pass