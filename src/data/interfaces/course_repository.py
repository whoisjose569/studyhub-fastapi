from abc import ABC, abstractmethod
from src.domain.models.courses import Courses
from typing import Optional

class CourseRepositoryInterface(ABC):
    
    @abstractmethod
    def insert_course(self, name: str, description: str, start_date) -> None:
        pass
    
    @abstractmethod
    def select_course(self, search: str = '') -> list[Courses]:
        pass
    
    @abstractmethod
    def select_course_by_id(self, id: int) -> Optional[Courses]:
        pass
    
    @abstractmethod
    def delete_course(self, id: int) -> dict:
        pass
    
    @abstractmethod
    def update_course(self, id: int, name: str, description: str) -> Optional[Courses]:
        pass
