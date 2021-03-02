# Class composition will be used more often than inheritance

class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f'Bookshelf with {len(self.books)} books.'


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Book {len(self.name)}'


book1 = Book('Harry Poter')
book2 = Book('Kind of Rings')


shelf = BookShelf(book1, book2)
print(shelf)
print(shelf.books)


# inheritance mean that a book is a bookshelf
# composition mean that bookshelf has bunch of books
