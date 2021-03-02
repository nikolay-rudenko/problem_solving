from typing import List


class Book:
    def __init__(self, name):
        self.name = name


    @staticmethod
    def hardcover(cls, weight: int) -> 'Book':
        return cls


class Bookshelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f'Bookshelf with {len(self.books)} books'


book = Book('Some book')
shelf = Bookshelf([book])
print(shelf)
print(Book('New').hardcover(book, 23), __name__)