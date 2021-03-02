
# 1 You import from the most relevant build in error class
# 2 You name in like you would like, you typing the custom message if you would like

class TooManyPagesReadError(Exception):
    pass


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return (
            f'<Book {self.name}, read {self.pages_read} pages of {self.page_count}>'
        )

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f'You\'ve tried to read {self.pages_read + pages}, but this book only has {self.page_count} pages.'
            )

        self.pages_read += pages
        return f'Now you read {self.pages_read} pages out of {self.page_count}'


try:
    python101 = Book('Python 101', 35)
    python101.read(154)
except TooManyPagesReadError as e:
    print(e)
