class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for i in self.books:
            if book.title == i.title and book.author == i.author:
                self.books.remove(i)

    def search_books(self, search_string):
        books_list = []
        for i in self.books:
            if search_string.lower() in i.title.lower() or search_string.lower() in i.author.lower():
                books_list.append(i)
        return books_list
