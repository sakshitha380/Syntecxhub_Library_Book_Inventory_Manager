from book import Book
from library import Library


def display_menu():
    """Display the main menu of the application."""
    print("\n" + "=" * 55)
    print("          LIBRARY BOOK INVENTORY MANAGER")
    print("=" * 55)
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book by Title")
    print("4. Search Book by Author")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Library Reports")
    print("8. Exit")
    print("=" * 55)


def add_book(library):
    """Add a new book to the library."""
    print("\n--- Add New Book ---")

    book_id = input("Enter Book ID: ").strip()
    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()
    year = input("Enter Publication Year: ").strip()

    # Validate empty fields
    if not book_id:
        print("Book ID is required.")
        return

    if not title:
        print("Book title is required.")
        return

    if not author:
        print("Author name is required.")
        return

    if not year:
        print("Publication year is required.")
        return

    # Validate publication year
    try:
        year = int(year)
    except ValueError:
        print("Publication year must be a number.")
        return

    if year <= 0:
        print("Publication year must be greater than 0.")
        return

    # Create Book object
    book = Book(book_id, title, author, year)

    # Add book to Library
    if library.add_book(book):
        print("\nBook added successfully!")
    else:
        print("\nA book with this ID already exists.")


def view_all_books(library):
    """Display all books in the library."""
    print("\n--- All Books ---")

    books = library.get_all_books()

    if not books:
        print("No books found in the library.")
        return

    print(f"\nTotal books: {len(books)}")
    print("-" * 100)

    for book in books:
        print(book)

    print("-" * 100)


def search_by_title(library):
    """Search books by title."""
    print("\n--- Search Book by Title ---")

    title = input("Enter title to search: ").strip()

    if not title:
        print("Search title cannot be empty.")
        return

    results = library.search_by_title(title)

    if not results:
        print("No books found with that title.")
        return

    print(f"\nFound {len(results)} book(s):")
    print("-" * 100)

    for book in results:
        print(book)

    print("-" * 100)


def search_by_author(library):
    """Search books by author."""
    print("\n--- Search Book by Author ---")

    author = input("Enter author name to search: ").strip()

    if not author:
        print("Search author cannot be empty.")
        return

    results = library.search_by_author(author)

    if not results:
        print("No books found for that author.")
        return

    print(f"\nFound {len(results)} book(s):")
    print("-" * 100)

    for book in results:
        print(book)

    print("-" * 100)


def issue_book(library):
    """Issue a book to a library member."""
    print("\n--- Issue Book ---")

    book_id = input("Enter Book ID: ").strip()
    member_name = input("Enter Member Name: ").strip()

    if not book_id:
        print("Book ID is required.")
        return

    if not member_name:
        print("Member name is required.")
        return

    success, message = library.issue_book(book_id, member_name)

    if success:
        print(f"\n{message}")
        print(f"Book {book_id} has been issued to {member_name}.")
    else:
        print(f"\n{message}")


def return_book(library):
    """Return an issued book to the library."""
    print("\n--- Return Book ---")

    book_id = input("Enter Book ID: ").strip()

    if not book_id:
        print("Book ID is required.")
        return

    success, message = library.return_book(book_id)

    if success:
        print(f"\n{message}")
    else:
        print(f"\n{message}")


def display_reports(library):
    """Display library statistics and reports."""
    print("\n" + "=" * 55)
    print("                  LIBRARY REPORT")
    print("=" * 55)

    total_books = library.get_total_books()
    available_books = library.get_available_count()
    issued_books = library.get_issued_count()

    print(f"Total Books     : {total_books}")
    print(f"Available Books : {available_books}")
    print(f"Issued Books    : {issued_books}")

    if total_books > 0:
        issued_rate = (issued_books / total_books) * 100
        print(f"Issued Rate     : {issued_rate:.1f}%")
    else:
        print("Issued Rate     : 0.0%")

    print("=" * 55)


def main():
    """Run the Library Book Inventory Manager."""
    library = Library()

    print("\n" + "=" * 55)
    print("     Welcome to Library Book Inventory Manager")
    print("=" * 55)

    while True:
        display_menu()

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_book(library)

        elif choice == "2":
            view_all_books(library)

        elif choice == "3":
            search_by_title(library)

        elif choice == "4":
            search_by_author(library)

        elif choice == "5":
            issue_book(library)

        elif choice == "6":
            return_book(library)

        elif choice == "7":
            display_reports(library)

        elif choice == "8":
            print("\n" + "=" * 55)
            print("Thank you for using Library Book Inventory Manager!")
            print("Goodbye!")
            print("=" * 55)
            break

        else:
            print("\nInvalid choice.")
            print("Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()