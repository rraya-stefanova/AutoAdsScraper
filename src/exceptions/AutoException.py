class AutoException(Exception):
    def __init__(self, response) -> None:
        super().__init__(response)

    def __str__(self) -> str:
        return "Exception thrown by TMDBException."