from pathlib import Path
from book import Book

LIBRARIAN_CODE = "2130"


def load_books(filename: str) -> list[Book]:
    """Load a comma-separated book catalogue into Book objects."""
    path = Path(filename)

    if not path.exists():
        raise FileNotFoundError(f"Book catalogue not found: {filename}")

    books: list[Book] = []
    with path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue

            parts = [part.strip() for part in line.split(",")]
            if len(parts) != 5:
                raise ValueError(
                    f"Invalid catalogue record on line {line_number}: expected 5 fields."
                )

            isbn, title, author, genre, availability = parts
            books.append(
                Book(
                    isbn,
                    title,
                    author,
                    int(genre),
                    availability.lower() == "available",
                )
            )
    return books


def save_books(book_list: list[Book], filename: str) -> int:
    """Persist the current catalogue to disk."""
    path = Path(filename)
    with path.open("w", encoding="utf-8") as file:
        for book in book_list:
            availability = (
                "available" if book.get_availability() == "Available" else "borrowed"
            )
            file.write(
                f"{book.get_isbn()},{book.get_title()},{book.get_author()},"
                f"{book.get_genre()},{availability}\n"
            )
    return len(book_list)


def find_book_by_isbn(book_list: list[Book], isbn: str) -> int:
    for index, book in enumerate(book_list):
        if book.get_isbn() == isbn:
            return index
    return -1


def print_catalog(book_list: list[Book]) -> None:
    print("\n{:<14} {:<28} {:<24} {:<20} {}".format(
        "ISBN", "Title", "Author", "Genre", "Availability"
    ))
    print("-" * 105)
    for book in book_list:
        print(book)


def add_book(book_list: list[Book]) -> None:
    isbn = input("ISBN: ").strip()
    if find_book_by_isbn(book_list, isbn) != -1:
        print("A book with that ISBN already exists.")
        return

    title = input("Title: ").strip()
    author = input("Author: ").strip()

    print("Genres:")
    for key, name in Book.genres.items():
        print(f"  {key}: {name}")

    try:
        genre = int(input("Genre number: ").strip())
    except ValueError:
        print("Genre must be a number.")
        return

    if genre not in Book.genres:
        print("Invalid genre.")
        return

    book_list.append(Book(isbn, title, author, genre, True))
    print(f"Added '{title}'.")


def remove_book(book_list: list[Book]) -> None:
    isbn = input("ISBN to remove: ").strip()
    index = find_book_by_isbn(book_list, isbn)
    if index == -1:
        print("No book found with that ISBN.")
        return

    removed = book_list.pop(index)
    print(f"Removed '{removed.get_title()}'.")


def update_availability(book_list: list[Book], borrow: bool) -> None:
    isbn = input("ISBN: ").strip()
    index = find_book_by_isbn(book_list, isbn)
    if index == -1:
        print("No book found with that ISBN.")
        return

    book = book_list[index]
    if borrow:
        if book.get_availability() == "Borrowed":
            print("That book is already borrowed.")
            return
        book.borrow_it()
        print(f"Borrowed '{book.get_title()}'.")
    else:
        if book.get_availability() == "Available":
            print("That book is already available.")
            return
        book.return_it()
        print(f"Returned '{book.get_title()}'.")


def prompt_for_catalogue() -> str:
    while True:
        filename = input("Book catalogue filename [books.csv]: ").strip() or "books.csv"
        if Path(filename).exists():
            return filename
        print("File not found. Try again.")


def main() -> None:
    print("Library Management System")
    print("=========================")

    filename = prompt_for_catalogue()
    book_list = load_books(filename)
    print(f"Loaded {len(book_list)} books from {filename}.")

    librarian = False

    while True:
        print("\nMenu")
        print("1. View catalogue")
        print("2. Borrow book")
        print("3. Return book")
        print("2130. Librarian mode")
        if librarian:
            print("4. Add book")
            print("5. Remove book")
        print("0. Save and exit")

        choice = input("Selection: ").strip()

        if choice == "1":
            print_catalog(book_list)
        elif choice == "2":
            update_availability(book_list, borrow=True)
        elif choice == "3":
            update_availability(book_list, borrow=False)
        elif choice == LIBRARIAN_CODE:
            librarian = True
            print("Librarian mode enabled.")
        elif librarian and choice == "4":
            add_book(book_list)
        elif librarian and choice == "5":
            remove_book(book_list)
        elif choice == "0":
            saved = save_books(book_list, filename)
            print(f"Saved {saved} books to {filename}.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
