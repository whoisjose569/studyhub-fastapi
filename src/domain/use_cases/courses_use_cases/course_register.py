from abc import ABC, abstractmethod

class CourseRegister(ABC):
    
    @abstractmethod
    def register(self, name: str, description: str, start_date) -> dict:
        pass