# 📚 Library Book Inventory Manager

A Python-based Library Book Inventory Manager developed as part of the **Syntecxhub Internship**.

This application allows users to manage library books, search books, issue and return books, view library reports, and permanently store book information using JSON.

---

## 📌 Project Overview

The Library Book Inventory Manager is a command-line application developed using Python and Object-Oriented Programming concepts.

The system provides basic library management functionality while demonstrating:

- Classes and objects
- Dictionaries
- Lists
- Iteration
- Searching
- File handling
- JSON data persistence
- Input validation
- Automated unit testing

---

## ✨ Features

### 📖 Book Management
- Add new books
- View all books
- Prevent duplicate Book IDs
- Store book details including:
  - Book ID
  - Title
  - Author
  - Publication Year
  - Availability Status
  - Issued Member

### 🔍 Search
- Search books by title
- Search books by author
- Supports partial and case-insensitive searches

### 📤 Issue Books
- Issue an available book to a library member
- Prevent issuing an already-issued book
- Store the member name

### 📥 Return Books
- Return an issued book
- Automatically update its availability status

### 📊 Library Reports
The application displays:

- Total number of books
- Available books
- Issued books
- Issued-book percentage

### 💾 JSON Persistence
Book information is stored in:

```text
data/books.json