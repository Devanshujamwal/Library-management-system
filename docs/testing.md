# Testing Notes

## Run the checks

```bash
python test_book.py
```

Expected result:

```text
All Book model checks passed.
```

## What is checked

The current assertions verify:

- object construction
- title retrieval
- genre mapping
- initial availability
- borrowing
- returning
- case-insensitive title matching
- setters
- updated genre handling

## What is not claimed

These checks do not represent full automated coverage of every CLI path, file-system error, or invalid user input. The README and portfolio deliberately distinguish verified model behaviour from broader application behaviour.

## Manual CLI validation

A useful manual pass is:

1. start `library_app.py`;
2. load the included `books.csv`;
3. view the catalogue;
4. borrow a book;
5. return a book;
6. enable librarian mode;
7. add and remove a record;
8. save and exit;
9. reopen the catalogue to confirm persistence.
