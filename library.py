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

        def load_data(self):
        # Start with the default books
         self.books = self.default_books.copy()

        if os.path.exists("books.csv"):
            with open("books.csv", "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.books[row["book_id"]] = {
                        "title": row["title"],
                        "author": row["author"],
                        "copies": int(row["copies"]),
                        "publish_year": int(row["publish_year"]),
                    }
            print("Books data loaded successfully!")

        if os.path.exists("users.csv"):
            with open("users.csv", "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    borrowed_books = eval(row["borrowed_books"])  # Convert string back to list of dicts
                    self.users[row["username"]] = {"section": row["section"], "borrowed_books": borrowed_books}
            print("Users data loaded successfully!")

        if os.path.exists("history.csv"):
            with open("history.csv", "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.history.append({
                        "username": row.get("username", "Unknown"),
                        "book_id": row.get("book_id", "Unknown"),
                        "quantity": int(row.get("quantity", 0)),
                        "borrow_date": row.get("borrow_date", "N/A"),
                        "return_date": row.get("return_date", "N/A"),
                        "remarks": row.get("remarks", "N/A"),
                    })
            print("History data loaded successfully!")
        else:
            print("No saved data found, starting with default books.")



def start(self):
        while True:
            print("\n------------------------------------------- WELCOME TO LIBRARY MANAGEMENT SYSTEM ------------------------------------------")
            print("[1] Librarian")
            print("[2] Student")
            user_type = input("Choose your role: ")
