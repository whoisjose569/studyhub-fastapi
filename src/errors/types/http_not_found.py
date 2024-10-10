class HttpNotFoundError(Exception):
    
    def __init__(self, message: str) -> None:
        self.message = message
        self.name = 'NotFound'
        self.status_code = 404
        super().__init__(self.message)