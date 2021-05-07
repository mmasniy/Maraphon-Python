def get_anonymous(books):
    new_books = []
    for title in books:
        if ' by ' not in title:
            new_books.append(title)

    return new_books
