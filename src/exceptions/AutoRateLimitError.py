class AutoRateLimitError(Exception):
    def __init__(self, response) -> None:
        super().__init__(response)

    def __str__(self) -> str:
        return "At rate limit."