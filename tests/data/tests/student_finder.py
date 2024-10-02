class StudentFinderSpy:
    def __init__(self) -> None:
        self.find_attributes = {}
    
    def find(self, search: str) -> dict:
        self.find_attributes["search"] = search
        
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