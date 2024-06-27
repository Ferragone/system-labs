# Початковий клас LibraryBook
class LibraryBook:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False

# Клас LibraryBookDetails для делегування додаткової функціональності
class LibraryBookDetails:
    def __init__(self, library_book):
        self.library_book = library_book

    def check_condition(self):
        # В даному прикладі ми просто повертаємо рядок, в реальному випадку можна додати реальну логіку
        return "Good condition"

    def get_info(self):
        return f"Title: {self.library_book.title}, Author: {self.library_book.author}, Year: {self.library_book.publication_year}"

# Використання коду
book = LibraryBook("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book_details = LibraryBookDetails(book)
print(book.check_out())
print(book.check_out())
print(book_details.get_info())
print(book_details.check_condition())