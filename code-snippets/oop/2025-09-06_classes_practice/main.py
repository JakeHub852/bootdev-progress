class Book:
    def __init__(self, title, author):
        # Simple data container for a book record
        self.title = title
        self.author = author 


class Library:
    def __init__(self, name):
        # Library name and an ordered collection of Book instances
        self.name = name
        self.books = []

    def add_book(self, book): 
        # Add a book to the end of the collection
        # Assumes 'book' is an instance of Book
        self.books.append(book)

    def remove_book(self, book): 
        # Remove all books that match both title and author
        # Build a new list instead of mutating while iterating
        books_to_keep = []
        for current_book in self.books:
            # Keep books that don't match both fields
            if current_book.title != book.title or current_book.author != book.author:
                books_to_keep.append(current_book)
        # Replace the original list to avoid skipped elements during removal
        self.books = books_to_keep
   
    def search_books(self, search_string): 
        # Case-insensitive substring search on title OR author
        # Returns results in insertion order
        results = []
        for book in self.books:
            if search_string.lower() in book.title.lower() or search_string.lower() in book.author.lower():
                results.append(book)
        return results