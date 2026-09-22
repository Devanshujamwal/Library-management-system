import book


def main():
    books = [
        book.Book("978-0441172719", "Dune", "Frank Herbert", 2, True),
        book.Book("978-0375822742", "The City of Ember", "Jeanne DuPrau", 4, True),
        book.Book("978-0060513030", "Where the Sidewalk Ends", "Shel Silverstein", 9, False),
    ]

    dune = books[0]
    assert dune.get_title() == "Dune"
    assert dune.get_genre_name() == "Science Fiction"
    assert dune.get_availability() == "Available"

    dune.borrow_it()
    assert dune.get_availability() == "Borrowed"

    matches = [b for b in books if "city" in b.get_title().lower()]
    assert len(matches) == 1
    assert matches[0].get_isbn() == "978-0375822742"

    last_book = books[-1]
    last_book.return_it()
    last_book.set_isbn("978-0394800165")
    last_book.set_title("Green Eggs and Ham")
    last_book.set_author("Dr. Seuss")
    last_book.set_genre(5)

    assert last_book.get_availability() == "Available"
    assert last_book.get_title() == "Green Eggs and Ham"
    assert last_book.get_genre_name() == "Children’s Fiction"

    print("All Book model checks passed.")


if __name__ == "__main__":
    main()
