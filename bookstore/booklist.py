import sqlite3


def _get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def list():
    conn = _get_db_connection()
    books = conn.execute('SELECT * FROM books').fetchall()
    conn.close()

    return books
