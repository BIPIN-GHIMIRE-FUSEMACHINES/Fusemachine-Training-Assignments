class Book:
    def __init__(self, title, author, isbn, genre, availability):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.availability = availability

    def __str__(self):
        print("." * 100)
        return f"Books title:{self.title} Author:{self.author} ISBN:{self.isbn} genre:{self.genre} availability:{self.availability}"


class LibraryCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, book_obj):
        self.books.append(book_obj)

    def get_book_details(self):
        for book in self.books:
            print(book)

    def check_available_books(self):
        for book in self.books:
            if book.availability == True:
                print(book)

    def borow_book(self, book_isbn):
        for book in self.books:
            if book.isbn == book_isbn and book.availability == True:
                print("This book is available to borrow.")
                print(book)
                book.availability = False
                break
            else:
                print("The book is not available to borrow.")
                break


book1 = Book("a", "b", 12, "c", True)
book2 = Book("ab", "bf", 13, "cd", False)
book3 = Book("ac", "bf", 14, "cer", True)
book4 = Book("ad", "ba", 15, "asdc", True)

# Test Cases for adding books

# print(book1)
# print(book2)
# print(book3)
# print(book4)

Catalog = LibraryCatalog()
Catalog.add_book(book1)
Catalog.add_book(book2)
Catalog.add_book(book3)
Catalog.add_book(book4)

Catalog.borow_book(12)

# Test Cases for borrowing books

# Catalog.get_book_details()
# Catalog.check_available_books()
# Catalog.borow_book(12)
# Catalog.get_book_details()
# Catalog.check_available_books()
