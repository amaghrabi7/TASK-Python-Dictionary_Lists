from books import books

print(books[0])
#  number_of_authors(book)
#  recieves a book dictionary
#  returns the number of authors that the book has
def number_of_authors(book):
    return len(book["authors"])


print(number_of_authors(books[0]))

#  get_book_by_id(book_id, books)
#  # receives a book id
#  # recieves a list of book dictionaries
#  # returns the book dictionary with the same id as the book_id provided
def get_book_by_id(book_id, books):
    for book in books:
        if book["id"] == book_id:
            return book


print(get_book_by_id(38, books))


# add_summary_to_book(summary, book)
# receives a book dictionary
# recieves a summary string
# adds the summary to the book dictionary
# return the book dictionary
def add_summary_to_book(summary, book):
    book["summary"] = summary
    return book


print(add_summary_to_book("this is a good book about", books[0]))


# CHALLENGE 1
# get_book_property(property, book)
# receives a book dictionary
# recieves a property (string)
# return the book property


def get_book_property(property, book):
    for key in book:
        if key == property:
            return book[property]


print(get_book_property("color", books[0]))
print(get_book_property("title", books[0]))


# CHALLENGE 2
# calculate_available_books(books)
# receives a list of books
# return a new list of unavailable books


def calculate_not_available_booknames(books):  # This function returns a list of unavailable book names
    available_books = []
    for book in books:
        if not book["available"]:
            available_books.append(book["title"])
    return available_books


print(calculate_not_available_booknames(books))

def calculate_not_available_books(books):  # This function returns a list of unavailable book dictionaries
    available_books = []
    for book in books:
        if not book["available"]:
            available_books.append(book)
    return available_books


print(calculate_not_available_books(books))


# CHALLENGE 3
# get_book_by_author_name(author_name, books)
# receives a author name (string)
# recieves a list of book dictionaries
# returns the book dictionary that contains an author with the author name provided

def get_book_by_author_name(author_name, books):
    books_by_author = [] 
    for book in books:
        authors = book["authors"]
        for author in authors:
            if author["name"] == author_name:
                books_by_author.append(book)
    
    return books_by_author

print(get_book_by_author_name("Neil Gaiman", books))
