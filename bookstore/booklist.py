import db


def list_books():
    conn = db.connect()
    books = conn.execute("SELECT * FROM books").fetchall()
    conn.close()
    return books


def add(books):
    conn = db.connect()
    for book in books:
        conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", (book[0], book[1]))
    books = conn.execute("SELECT * FROM books").fetchall()
    conn.commit()
    conn.close()
    return books
