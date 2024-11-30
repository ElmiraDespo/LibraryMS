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

# Display books in a formatted table
    def display_books(self):
        if not self.books:
            print("No books available in the library.")
            return

        # Print table header
        print("\n------------------------------------------------------ LIBRARY BOOKS ------------------------------------------------------")
        print(f"{'Book ID':<10} {'Book Title':<40} {'Author':<25} {'Copies':<10} {'Published Year':<15}")
        print("-" * 123)       

        # Print each book's details
        for book_id, details in self.books.items():
            print(f"{book_id:<10} {details['title']:<40} {details['author']:<25} {details['copies']:<10} {details['publish_year']:<15}")   
        print("\n---------------------------------------------------------------------------------------------------------------------------")

    # Add Book
    def add_book(self, book_id, title, author, copies, publish_year):
        if book_id not in self.books:
            self.books[book_id] = {
                "title": title,
                "author": author,
                "copies": copies,
                "publish_year": publish_year,
            }
            print(f"Book '{title}' added successfully!")
            self.save_data()  # Save data after changes
        else:
            print("Book already exists.")

    # Add User
    def add_user(self, username, section):
        if username not in self.users:
            # Add the user and initialize their borrowed books as an empty list
            self.users[username] = {"section": section, "borrowed_books": []}
            print(f"User '{username}' from Section '{section}' added successfully!")
            self.save_data()  # Save data after changes
        else:
            print("User already exists.")

    # Borrow Book
    def borrow_book(self, username, book_id, quantity, return_date):
        if username not in self.users:
            print("User not found. Please add the user first.")
            return

        if book_id in self.books and self.books[book_id]["copies"] >= quantity:
            self.books[book_id]["copies"] -= quantity
            borrow_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.users[username]["borrowed_books"].append({
                "book_id": book_id,
                "quantity": quantity,
                "borrow_date": borrow_date,
                "return_date": return_date,
                "remarks": "Borrowed",
            })
            self.history.append({
                "username": username,
                "book_id": book_id,
                "quantity": quantity,
                "borrow_date": borrow_date,
                "return_date": return_date,
                "remarks": "Borrowed",
            })
            print(f"Book '{self.books[book_id]['title']}' borrowed successfully!")
            self.save_data()  # Save data after changes
        else:
            print("Not enough copies available or book does not exist.")

    # Return Book
    def return_book(self, username, book_id, quantity):
        if username in self.users:
            borrowed_books = self.users[username]["borrowed_books"]
            for record in borrowed_books:
                if record["book_id"] == book_id and record["quantity"] == quantity:
                    borrowed_books.remove(record)  # Remove from user's borrowed list
                    self.books[book_id]["copies"] += quantity  # Return copies
                    return_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    overdue = self.check_overdue(record["return_date"])
                    remarks = "Overdue" if overdue else "Returned"
                    self.history.append({
                        "username": username,
                        "book_id": book_id,
                        "quantity": quantity,
                        "return_date": return_date,
                        "remarks": remarks,
                    })
                    print(f"Book '{self.books[book_id]['title']}' returned successfully!")
                    self.save_data()  # Save data after changes
                    return
            print("This book was not borrowed by the user or quantity mismatched.")
        else:
            print("User not found.")

     # Delete Book (Librarian only)
    def delete_book(self, password, book_id):
        if password == self.librarian_password:
            if book_id in self.books:
                del self.books[book_id]
                print(f"Book with ID '{book_id}' deleted successfully.")
                self.save_data()  # Save data after deletion
            else:
                print("Book not found.")
        else:
            print("Incorrect librarian password.")
            
    # Check Overdue
    def check_overdue(self, return_date):
        current_date = datetime.datetime.now()
        return_date_obj = datetime.datetime.strptime(return_date, "%Y-%m-%d %H:%M:%S")
        return current_date > return_date_obj  # Returns True if overdue

def start(self):
        while True:
            print("\n------------------------------------------- WELCOME TO LIBRARY MANAGEMENT SYSTEM ------------------------------------------")
            print("[1] Librarian")
            print("[2] Student")
            user_type = input("Choose your role: ")
