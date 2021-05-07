def add_to_bookshelf(book_to_add, bookshelf):
    try:
        bookshelf[bookshelf.index('---')] = book_to_add
    except ValueError:
        return False
    else:
        return True
