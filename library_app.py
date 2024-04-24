from book import Book
import os

def load_books(book_list):
    filename = input("Enter book catalog filename: ")

    while not os.path.exists(filename):
        print("File not found. Re-enter book catalog filename: ", end="")
        filename = input("")
    
    FILE = filename
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            isbn, title, author, genre, available = parts
            genre = int(genre)
            available = available.lower() == 'available'
            book_list.append(Book(isbn, title, author, genre, available))
    return len(book_list)

def find_book_by_isbn(book_list, isbn):
    for i, book in enumerate(book_list):
        if book.get_isbn() == isbn:
            return i
    return -1

def print_menu(menu_heading, menu_options):
    print("\n" + menu_heading)
    print("=" * len(menu_heading))
    for key, value in menu_options.items():
        print(f"{key}. {value}")
    return input("Enter your selection: ")

def add_book(book_list):
    isbn = input("-- Add a book --\nEnter the 13-digit ISBN (format 999-9999999999): ")
    title = input("Enter title: ")
    author = input("Enter author name: ")
    valid_genre = False  # Flag variable to control the loop
    arr = []

    for i in Book.genres.values():
        arr.append(i.capitalize())

    while not valid_genre:  # Loop runs as long as valid_genre is False
        genre_input = input("Enter genre: ")
        if genre_input.capitalize() in arr:
            genre = arr.index(genre_input.capitalize())
            valid_genre = True  # Set valid_genre to True to exit the loop
        else:
            print("Invalid genre. Choices are:", ", ".join(Book.genres.values()))
    book_list.append(Book(isbn, title, author, genre, True))
    print(f"'{title}' with ISBN {isbn} successfully added.")

def remove_book(book_list):
    isbn = input("-- Remove a book --\nEnter the 13-digit ISBN (format 999-9999999999): ")
    index = find_book_by_isbn(book_list, isbn)
    if index != -1:
        print(f"'{book_list[index].get_title()}' with ISBN {book_list[index].get_isbn()} successfully removed.")
        del book_list[index]
    else:
        print("No book found with that ISBN.")

# Function to save the list of books back to the file
def save_books(book_list):
    if not os.access(os.path.dirname(FILE), os.W_OK):
        
        return 0

    file = open(FILE, 'w')


    for book in book_list:


        # Writing book information to the file
        file.write(f"{book.get_isbn()},{book.get_title()},{book.get_author()},{book.get_genre()},{book.get_availability()}\n")
    file.close()
    return len(book_list)

def main():
    print("Starting the system ...")
    book_list = []
    if load_books(book_list):
        print("Book catalog has been loaded.")

        exit_system = False  # Flag variable to control the main loop
        librarian = False
        choice = 0
        while not exit_system:  # Loop runs as long as exit_system is False
            choice = input("Enter your selection: ")

            if librarian and choice == '4':
                isValid = True
                add_book(book_list)
            elif librarian and choice == '5':
                isValid = True
                remove_book(book_list)
            elif choice == '2130':
                isValid = True
                librarian = True
            else:
                isValid = False
                print("Invalid option")

if __name__ == "__main__":
    main()