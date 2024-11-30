import datetime
import csv
import os

class LibrarySystem:
    def __init__(self):
        # Predefined books in the library (always available even if no CSV file exists)
        self.default_books = {
            "B001": {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "copies": 5, "publish_year": 1997},
            "B002": {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "copies": 3, "publish_year": 1925},
            "B003": {"title": "1984", "author": "George Orwell", "copies": 4, "publish_year": 1949},
        }
        
        self.books = {}
        self.users = {}
        self.history = []
        self.librarian_password = "library"
        self.load_data()  # Load data from CSV or use default data if no CSV exists

    # Show Menu for Librarians
    def show_librarian_menu(self):
        print("\n---------------------------------------------------- LIBRARIAN ACCESS -----------------------------------------------------")
        print("1. Display All Books")
        print("2. Add Book")
        print("3. Add User")
        print("4. View Borrowing/Returning History")
        print("5. View Registered Users")
        print("6. Delete Book")  # New option added to delete book
        print("7. Exit")
    #SHOW MENU FOR STUDENTS
    def show_user_menu(self):
        print("\n---------------------------------------------------- STUDENT ACCESS -------------------------------------------------------")
        print("1. Display All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")

    # Save data to CSV files
    def save_data(self):
        # Save books data
        with open("books.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["book_id", "title", "author", "copies", "publish_year"])
            writer.writeheader()
            for book_id, details in self.books.items():
                writer.writerow({"book_id": book_id, **details})
        
        # Save users data
        with open("users.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["username", "section", "borrowed_books"])
            writer.writeheader()
            for username, details in self.users.items():
                writer.writerow({"username": username, "section": details["section"], "borrowed_books": str(details["borrowed_books"])})

        # Save history data
        with open("history.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["username", "book_id", "quantity", "borrow_date", "return_date", "remarks"])
            writer.writeheader()
            for record in self.history:
                writer.writerow({
                    "username": record.get("username", "Unknown"),
                    "book_id": record.get("book_id", "Unknown"),
                    "quantity": record.get("quantity", 0),
                    "borrow_date": record.get("borrow_date", "N/A"),
                    "return_date": record.get("return_date", "N/A"),
                    "remarks": record.get("remarks", "N/A"),
                })

        print("Data saved successfully!")

        
def start(self):
        while True:
            print("\n------------------------------------------- WELCOME TO LIBRARY MANAGEMENT SYSTEM ------------------------------------------")
            print("[1] Librarian")
            print("[2] Student")
            user_type = input("Choose your role: ")
