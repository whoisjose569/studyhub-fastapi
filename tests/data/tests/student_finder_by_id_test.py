class StudentFinderByIdSpy:
    def __init__(self) -> None:
        self.find_attributes = {}
    
    def find_by_id(self, id: int) -> dict:
        self.find_attributes["id"] = 1
        
        return {
            "type": "Students",
            "count": 1,
            "students": [{
                "id": 1,
                "name": 'test',
                "email": 'test@email',
                "enrollment_date": '2024-08-10'
            }]
        }