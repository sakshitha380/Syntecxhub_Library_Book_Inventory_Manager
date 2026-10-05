import os
import tempfile
import unittest

from book import Book
from library import Library


class TestLibrary(unittest.TestCase):

    def setUp(self):
        """Create a temporary library for each test."""
        self.temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".json"
        )
        self.temp_file.close()

        self.library = Library(self.temp_file.name)

    def tearDown(self):
        """Remove the temporary JSON file after each test."""
        if os.path.exists(self.temp_file.name):
            os.remove(self.temp_file.name)

    def test_add_book(self):
        """Test adding a new book."""
        book = Book(
            "B001",
            "Python Programming",
            "Mark Lutz",
            2024
        )

        result = self.library.add_book(book)

        self.assertTrue(result)
        self.assertEqual(self.library.get_total_books(), 1)

    def test_duplicate_book_id(self):
        """Test that duplicate Book IDs are rejected."""
        book1 = Book(
            "B001",
            "Python Programming",
            "Mark Lutz",
            2024
        )

        book2 = Book(
            "B001",
            "Data Structures",
            "Narasimha Karumanchi",
            2023
        )

        self.assertTrue(self.library.add_book(book1))
        self.assertFalse(self.library.add_book(book2))

        self.assertEqual(
            self.library.get_total_books(),
            1
        )

    def test_search_by_title(self):
        """Test searching books by title."""
        book = Book(
            "B001",
            "Python Programming",
            "Mark Lutz",
            2024
        )

        self.library.add_book(book)

        results = self.library.search_by_title("python")

        self.assertEqual(len(results), 1)
        self.assertEqual(
            results[0].title,
            "Python Programming"
        )

    def test_search_by_author(self):
        """Test searching books by author."""
        book = Book(
            "B001",
            "Python Programming",
            "Mark Lutz",
            2024
        )

        self.library.add_book(book)

        results = self.library.search_by_author("mark")

        self.assertEqual(len(results), 1)
        self.assertEqual(
            results[0].author,
            "Mark Lutz"
        )

    def test_issue_book(self):
        """Test issuing an available book."""
        book = Book(
            "B001",
            "Python Programming",
            "Mark Lutz",
            2024
        )

        self.library.add_book(book)

        success, message = self.library.issue_book(
            "B001",
            "Lasya"
        )

        self.assertTrue(success)
        self.assertEqual(
            message,
            "Book issued successfully."
        )

        self.assertEqual(
            self.library.books["B001"].status,
            "Issued"
        )

        self.assertEqual(
            self.library.books["B001"].issued_to,
            "Lasya"
        )

    def test_issue_already_issued_book(self):
        """Test that an issued book cannot be issued again."""
        book = Book(
            "B001",
            "Python Programming",
            "Mark Lutz",
            2024
        )

        self.library.add_book(book)

        self.library.issue_book(
            "B001",
            "Lasya"
        )

        success, message = self.library.issue_book(
            "B001",
            "Another Member"
        )

        self.assertFalse(success)
        self.assertEqual(
            message,
            "Book is already issued."
        )

    def test_return_book(self):
        """Test returning an issued book."""
        book = Book(
            "B001",
            "Python Programming",
            "Mark Lutz",
            2024
        )

        self.library.add_book(book)

        self.library.issue_book(
            "B001",
            "Lasya"
        )

        success, message = self.library.return_book("B001")

        self.assertTrue(success)
        self.assertEqual(
            message,
            "Book returned successfully."
        )

        self.assertEqual(
            self.library.books["B001"].status,
            "Available"
        )

        self.assertIsNone(
            self.library.books["B001"].issued_to
        )

    def test_book_counts(self):
        """Test total, available, and issued book counts."""
        book1 = Book(
            "B001",
            "Python Programming",
            "Mark Lutz",
            2024
        )

        book2 = Book(
            "B002",
            "Data Structures",
            "Narasimha Karumanchi",
            2023
        )

        self.library.add_book(book1)
        self.library.add_book(book2)

        self.assertEqual(
            self.library.get_total_books(),
            2
        )

        self.assertEqual(
            self.library.get_available_count(),
            2
        )

        self.library.issue_book(
            "B001",
            "Lasya"
        )

        self.assertEqual(
            self.library.get_issued_count(),
            1
        )

        self.assertEqual(
            self.library.get_available_count(),
            1
        )

    def test_json_persistence(self):
        """Test saving and loading books from JSON."""
        book = Book(
            "B001",
            "Python Programming",
            "Mark Lutz",
            2024
        )

        self.library.add_book(book)

        new_library = Library(
            self.temp_file.name
        )

        self.assertEqual(
            new_library.get_total_books(),
            1
        )

        loaded_book = new_library.books["B001"]

        self.assertEqual(
            loaded_book.title,
            "Python Programming"
        )

        self.assertEqual(
            loaded_book.author,
            "Mark Lutz"
        )

        self.assertEqual(
            loaded_book.year,
            2024
        )


if __name__ == "__main__":
    unittest.main()