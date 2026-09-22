# Application Architecture

The project separates library-record behaviour from the command-line workflow.

```text
User
 |
 v
library_app.py
 |       \
 |        \--> books.csv
 v
book.py
(Book class)

test_book.py --> book.py
```

## Book model

`book.py` encapsulates:

- ISBN
- title
- author
- genre
- availability

It also provides behaviour for borrowing, returning, updating fields, and displaying a formatted record.

## Application layer

`library_app.py` handles:

- catalogue loading
- catalogue saving
- ISBN lookup
- viewing records
- borrowing/returning
- librarian add/remove operations
- command-line interaction

## Persistence

The refreshed version passes the catalogue filename explicitly between load/save operations instead of relying on a variable with incorrect scope.

## Testing

`test_book.py` contains repeatable assertions for key Book-model behaviour. It is intentionally small and focused on the core class rather than claiming full end-to-end application coverage.
