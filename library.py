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
        
def start(self):
        while True:
            print("\n------------------------------------------- WELCOME TO LIBRARY MANAGEMENT SYSTEM ------------------------------------------")
            print("[1] Librarian")
            print("[2] Student")
            user_type = input("Choose your role: ")
