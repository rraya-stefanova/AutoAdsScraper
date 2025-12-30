class AutoNotFoundError(Exception):
    def __init__(self, response) -> None:
        super().__init__(response)

    def __str__(self) -> str:
        return "Resource not found."