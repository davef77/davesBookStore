import os
import sqlite3

DATA_PATH = "/app/bookstore_db"


CREATE_TABLE = """CREATE TABLE IF NOT EXISTS books 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, author TEXT NOT NULL)"""


def connect():
    conn = sqlite3.connect(os.path.join(DATA_PATH, 'bookstore.db'))
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    if not os.path.exists(DATA_PATH):
        os.mkdir(DATA_PATH)

    conn = connect()

    cur = conn.cursor()
    cur.execute(CREATE_TABLE)

    add_sample_records(cur)

    conn.commit()
    conn.close()
    print('Initialized the database.')


def is_empty(cur):
    cur.execute('select * from books;')
    return len(cur.fetchall()) == 0


def add_sample_records(cur):
    if is_empty(cur):
        cur.execute("INSERT INTO books (title, author) VALUES (?, ?)",
                    ('Continuous Delivery', 'Dave Farley & Jez Humble'))
        cur.execute("INSERT INTO books (title, author) VALUES (?, ?)",
                    ('CD Pipelines', 'Dave Farley'))
        cur.execute("INSERT INTO books (title, author) VALUES (?, ?)",
                    ('Modern Software Engineering', 'Dave Farley'))