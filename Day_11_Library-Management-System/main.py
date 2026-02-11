#          DAY-11
# Library Management System (add/remove books, check availability).
book_list = [
    {"title": "Harry Potter", "author": "J.K. Rowling"},
    {"title": "Atomic Habits", "author": "James Clear"},
    {"title": "The Lord of the Rings", "author": "J.R.R."},
    {"title": "Lord of the Flies", "author": "William Golding"},
    {"title": "A Tale of Two Cities", "author": "Charles Dickens"},
]

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    new_book = {"title": title, "author": author}
    book_list.append(new_book)
    print(f"Book '{title}' added successfully!")

def remove_book():
    title = input("Enter book title to remove: ").strip()
    for book in book_list:
        if book["title"].lower() == title.lower():
            book_list.remove(book) 
            print(f"Book '{title}' removed successfully ❌")
            break
    else:
        print(f"Book '{title}' not found in the library!")

def check_availability():
    title = input("Enter book title to check: ").strip()
    for book in book_list:
        if book["title"].lower() == title.lower():
            print(f"'{title}' is available in the library 📚")
            break
    else:
        print(f"Book '{title}' is not available in the library ")

def view_books():
    if not book_list:
        print("No books in the library yet!")
        return
    print("Books in Library:")
    for book in book_list:
        print(f"{book['title']} — {book['author']}")

game = False

while not game:
    print("---- Library Management System ----")
    options = ["1. Add Book", "2. Remove Book", "3. Check Availability", "4. View Books", "5. Exit",]
    for el in options:
        print(el)


    ask = input("\nEnter your choice: ")
    if ask == "1":
        add_book()
    elif ask == "2":
        print("Before: ", book_list)
        remove_book()
        print("After: ", book_list)
    elif ask == "3":
        check_availability()
    elif ask == "4":
        view_books()
    elif ask == "5":
        print("Goodbye! 👋")
        game = True
    else:
        print("Please make a valid choice from the available options!")