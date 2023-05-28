class Library():

    def __init__(self, no_of_books, *books):
        self.books = books
        self.books = list(self.books)
        self.no_of_books = no_of_books # instance variables

    @property # This is a getter
    def add_books(self):
        return self.books

    @add_books.setter # This is a setter
    def add_books(self, book):
        self.books.append(book)
        self.no_of_books += 1

    def showBooks(self):
        print("The books are...")
        for book in self.books:
            print(book)
        # print(f"The number of books are {self.no_of_books}")
    
    def check_book_no(self):
        if self.no_of_books != len(self.books):
            print("The number of books you entered is not equal to the length of of books! You may have made a mistake")

zlib = Library(4, 'Harry Potter', 'A Song Of Fire And Ice', 'Invisible Man', 'War Of The World', 'Learn C The Hard Way')

zlib.add_books = 'Sherlock Holmes'

# print(zlib.add_books) # It Prints the name of books as tuple
zlib.showBooks()
print()
zlib.check_book_no()
