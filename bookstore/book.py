class Book:
    def __init__(self, book_id, name, author, price):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.book_id},{self.name},{self.author},{self.price}"