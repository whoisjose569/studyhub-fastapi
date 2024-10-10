class HttpConflictError(Exception):
    def __init__(self, message: str):
        self.status_code = 409
        self.name = "Conflict"
        self.message = message