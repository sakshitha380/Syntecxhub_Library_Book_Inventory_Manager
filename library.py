import json
import os

from book import Book


class Library:
    def __init__(self, data_file="data/books.json"):
        self.books = {}
        self.data_file = data_file

        self.load_data()

    def add_book(self, book):
        if book.book_id in self.books:
            return False

        self.books[book.book_id] = book
        self.save_data()

        return True

    def get_all_books(self):
        return list(self.books.values())

    def search_by_title(self, title):
        results = []

        for book in self.books.values():
            if title.lower() in book.title.lower():
                results.append(book)

        return results

    def search_by_author(self, author):
        results = []

        for book in self.books.values():
            if author.lower() in book.author.lower():
                results.append(book)

        return results

    def issue_book(self, book_id, member_name):
        if book_id not in self.books:
            return False, "Book not found."

        book = self.books[book_id]

        if book.status == "Issued":
            return False, "Book is already issued."

        book.issue(member_name)
        self.save_data()

        return True, "Book issued successfully."

    def return_book(self, book_id):
        if book_id not in self.books:
            return False, "Book not found."

        book = self.books[book_id]

        if book.status == "Available":
            return False, "Book is already available."

        book.return_book()
        self.save_data()

        return True, "Book returned successfully."

    def get_total_books(self):
        return len(self.books)

    def get_issued_count(self):
        count = 0

        for book in self.books.values():
            if book.status == "Issued":
                count += 1

        return count

    def get_available_count(self):
        count = 0

        for book in self.books.values():
            if book.status == "Available":
                count += 1

        return count

    def save_data(self):
        data = []

        for book in self.books.values():
            data.append(book.to_dict())

        directory = os.path.dirname(self.data_file)

        if directory:
            os.makedirs(directory, exist_ok=True)

        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        if not os.path.exists(self.data_file):
            return

        try:
            with open(self.data_file, "r", encoding="utf-8") as file:
                data = json.load(file)

            for book_data in data:
                book = Book.from_dict(book_data)
                self.books[book.book_id] = book

        except (json.JSONDecodeError, TypeError):
            print("Warning: Could not load library data.")
            self.books = {}