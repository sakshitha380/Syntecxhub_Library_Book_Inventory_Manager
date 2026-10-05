class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = "Available"
        self.issued_to = None

    def issue(self, member_name):
        self.status = "Issued"
        self.issued_to = member_name

    def return_book(self):
        self.status = "Available"
        self.issued_to = None

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
            "issued_to": self.issued_to
        }

    @classmethod
    def from_dict(cls, data):
        book = cls(
            data["book_id"],
            data["title"],
            data["author"],
            data["year"]
        )

        book.status = data.get("status", "Available")
        book.issued_to = data.get("issued_to")

        return book

    def __str__(self):
        issued_info = self.issued_to if self.issued_to else "None"
        return (
            f"ID: {self.book_id} | "
            f"Title: {self.title} | "
            f"Author: {self.author} | "
            f"Year: {self.year} | "
            f"Status: {self.status}"
        )