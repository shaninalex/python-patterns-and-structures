import json
from pydantic import BaseModel, model_validator, field_validator
from typing import Optional, List


class ISBN10FormatError(Exception):
    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)


class ISBNMissingError(Exception):
    def __init__(self, title: str, message: str) -> None:
        self.title = title
        self.message = message
        super().__init__(message)


class Book(BaseModel):
    title: str
    author: str
    publicher: str
    price: float
    subtitle: Optional[str] = None
    isbn_10: Optional[str] = None
    isbn_13: Optional[str] = None

    @model_validator(mode="before")
    @classmethod
    def check_isbn10_or_isbn13(cls, values):
        if "isbn_10" not in values and "isbn_13" not in values:
            raise ISBNMissingError(
                title=values["title"],
                message="Document should have either an ISBN10 or ISBN13"
            )
    
        return values

    @field_validator("isbn_10")
    @classmethod
    def isbn_10_valid(cls, value) -> None:
        chars = [c for c in value if c in "0123456789Xx"]
        if len(chars) != 10:
            raise ISBN10FormatError(value=value, message="ISBN10 shoud be 10 digits.")

        def char_to_int(char: str) -> int:
            if char in "Xx":
                return 10
            return int(char)

        weighted_sum = sum((10 - i) * char_to_int(x) for i, x in enumerate(chars))
        if weighted_sum % 11 != 0:
            raise ISBN10FormatError(
                value=value, message="ISBN10 digit sum should be divisible by 11."
            )

        return value

def main():
    with open("./books.json") as file:
        data = json.load(file)
        books: List[Book] = [Book(**item) for item in data]
        print(books)


if __name__ == "__main__":
    main()
