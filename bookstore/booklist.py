import sqlite3


def _get_db_connection():
    # conn = sqlite3.connect('../../bookstore/database.db')
    conn = sqlite3.connect('/app/bookstore/database.db')
    conn.row_factory = sqlite3.Row
    return conn


def list_books():
    conn = _get_db_connection()
    books = conn.execute("SELECT * FROM books").fetchall()
    conn.close()
    return books


def add(books):
    print("Got to booklist.add book")
    conn = _get_db_connection()
    conn.executemany('INSERT INTO books ("title", "author") VALUES(?,?);', books)
    books = conn.execute("SELECT * FROM books").fetchall()
    conn.close()
    return books

