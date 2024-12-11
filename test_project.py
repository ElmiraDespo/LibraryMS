import pytest
import os
import datetime
from unittest.mock import patch, mock_open
from project import LibrarySystem  # Replace this with the correct import if the code is in another file

@pytest.fixture
def library_system():
    """Fixture to initialize a LibrarySystem instance."""
    # Mock file existence and content
    mock_files = {
        "books.csv": "book_id,title,author,copies,publish_year\nB001,Harry Potter and the Sorcerer's Stone,J.K. Rowling,5,1997",
        "users.csv": "username,section,borrowed_books\n",
        "history.csv": "username,book_id,quantity,borrow_date,return_date,remarks\n",
    }
    
    def mock_open_side_effect(filepath, *args, **kwargs):
        # Return mocked file content based on file path
        filename = os.path.basename(filepath)
        if filename in mock_files:
            return mock_open(read_data=mock_files[filename])()
        else:
            return mock_open(read_data="")()
    
    with patch("builtins.open", new_callable=mock_open) as mocked_open, \
         patch("os.path.exists", return_value=True):
        mocked_open.side_effect = mock_open_side_effect
        return LibrarySystem()


# Test cases
def test_initial_books(library_system):
    """Test that the initial books are loaded correctly."""
    assert len(library_system.books) == 3
    assert "B001" in library_system.books
    assert library_system.books["B001"]["title"] == "Harry Potter and the Sorcerer's Stone"

def test_add_user(library_system):
    """Test adding a user."""
    library_system.add_user("testuser", "Test Section")
    assert "testuser" in library_system.users
    assert library_system.users["testuser"]["section"] == "Test Section"
    assert library_system.users["testuser"]["borrowed_books"] == []

def test_add_book(library_system):
    """Test adding a book."""
    library_system.add_book("B004", "New Book", "Test Author", 10, 2020)
    assert "B004" in library_system.books
    assert library_system.books["B004"]["title"] == "New Book"

def test_borrow_book(library_system):
    """Test borrowing a book."""
    library_system.add_user("testuser", "Test Section")
    return_date = (datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S")
    library_system.borrow_book("testuser", "B001", 1, return_date)
    assert library_system.books["B001"]["copies"] == 4
    assert len(library_system.users["testuser"]["borrowed_books"]) == 1
    assert library_system.users["testuser"]["borrowed_books"][0]["book_id"] == "B001"

def test_return_book(library_system):
    """Test returning a book."""
    library_system.add_user("testuser", "Test Section")
    return_date = (datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S")
    library_system.borrow_book("testuser", "B001", 1, return_date)
    library_system.return_book("testuser", "B001", 1)
    assert library_system.books["B001"]["copies"] == 5
    assert len(library_system.users["testuser"]["borrowed_books"]) == 0

def test_delete_book(library_system):
    """Test deleting a book."""
    library_system.delete_book("library", "B001")
    assert "B001" not in library_system.books

def test_view_users(library_system, capsys):
    """Test viewing registered users."""
    library_system.add_user("testuser", "Test Section")
    library_system.view_users()
    captured = capsys.readouterr()
    assert "testuser" in captured.out
    assert "Test Section" in captured.out

def test_view_history(library_system, capsys):
    """Test viewing history."""
    library_system.add_user("testuser", "Test Section")
    return_date = (datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S")
    library_system.borrow_book("testuser", "B001", 1, return_date)
    library_system.view_history("library")
    captured = capsys.readouterr()
    assert "testuser" in captured.out
    assert "B001" in captured.out

def test_invalid_librarian_password(library_system, capsys):
    """Test invalid librarian password."""
    library_system.view_history("wrongpassword")
    captured = capsys.readouterr()
    assert "Incorrect password" in captured.out
