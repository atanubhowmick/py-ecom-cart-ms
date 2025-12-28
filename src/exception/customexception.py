class ApplicationException(Exception):
    """Create custom exception for exception handling"""

    def __init__(self, error_code: str, error_message: str, http_status_code: int):
        self.error_code = error_code
        self.error_message = error_message
        self.http_status_code = http_status_code
        super().__init__(self.error_message)