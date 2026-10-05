# 📚 Library Book Inventory Manager

A Python command-line Library Book Inventory Manager developed as part of the **Syntecxhub Internship**.

## 📌 Overview

This project manages library books and demonstrates Python, Object-Oriented Programming, collections, iteration, file handling, JSON persistence, validation, and automated testing.

## ✨ Features

- Add new books
- View all books
- Search books by title
- Search books by author
- Prevent duplicate Book IDs
- Issue books to members
- Prevent issuing an already-issued book
- Return books
- View library reports
- Store and reload data using JSON
- Input validation
- Automated unit tests

## 🛠️ Technologies

- Python 3
- Object-Oriented Programming
- JSON
- `unittest`
- File Handling
- Lists and Dictionaries
- VS Code
- Git and GitHub

## 📂 Project Structure

```text
Syntecxhub_Library_Book_Inventory_Manager/
├── data/
│   └── books.json
├── tests/
│   └── test_library.py
├── .gitignore
├── app.py
├── book.py
├── library.py
└── README.md
```

`venv/` is used locally and is excluded from GitHub by `.gitignore`.

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/sakshitha380/Syntecxhub_Library_Book_Inventory_Manager.git
cd Syntecxhub_Library_Book_Inventory_Manager
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate it on Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Run the application

```bash
python app.py
```

## 🖥️ Application Menu

```text
=======================================================
          LIBRARY BOOK INVENTORY MANAGER
=======================================================
1. Add Book
2. View All Books
3. Search Book by Title
4. Search Book by Author
5. Issue Book
6. Return Book
7. Library Reports
8. Exit
=======================================================
```

## 💾 JSON Persistence

Book data is stored in:

```text
data/books.json
```

The application loads saved books when it starts and saves changes when books are added, issued, or returned. This allows data to remain available after restarting the application.

## 🧱 Object-Oriented Design

### `Book` class

Represents an individual book and stores:

- Book ID
- Title
- Author
- Publication Year
- Status
- Issued Member

It provides methods for issuing, returning, converting data to a dictionary, and restoring a book from JSON data.

### `Library` class

Manages the collection of books and provides methods for:

- Adding books
- Searching by title and author
- Issuing and returning books
- Counting books
- Saving and loading JSON data

Books are stored in a Python dictionary using the Book ID as the key.

## 📦 Python Concepts Demonstrated

- **Lists:** store search results and JSON data.
- **Dictionaries:** provide Book ID based lookup.
- **Iteration:** process books using `for` loops.
- **Classes and Objects:** implemented through `Book` and `Library`.
- **File Handling:** reads and writes JSON files.
- **JSON:** provides persistent storage.
- **Exception Handling:** handles invalid JSON and invalid input.

## 🧪 Testing

Run all automated tests with:

```bash
python -m unittest discover -s tests -v
```

The project contains **9 automated tests**.

Expected result:

```text
Ran 9 tests

OK
```

### Functional Testing

| Feature | Status |
|---|---|
| Add Book | ✅ Passed |
| View All Books | ✅ Passed |
| Search by Title | ✅ Passed |
| Search by Author | ✅ Passed |
| Issue Book | ✅ Passed |
| Return Book | ✅ Passed |
| Library Reports | ✅ Passed |
| Exit Application | ✅ Passed |
| JSON Persistence | ✅ Passed |
| Automated Tests | ✅ 9/9 Passed |

## 🎯 Internship Project

Developed as part of the **Syntecxhub Internship** to demonstrate practical Python programming, Object-Oriented Programming, data persistence, testing, and GitHub project development.

## 👩‍💻 Author

**Sakshitha Ayyala**

B.E. Artificial Intelligence and Data Science

## 📜 License

This project is created for educational and internship purposes.
