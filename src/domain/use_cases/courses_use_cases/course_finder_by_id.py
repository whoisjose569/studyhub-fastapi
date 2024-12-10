from abc import ABC, abstractmethod

class CourseFinderById(ABC):
    
    @abstractmethod
    def find_by_id(self, id: int) -> dict:
        pass