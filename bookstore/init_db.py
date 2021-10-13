import sqlite3

connection = sqlite3.connect('bookstore_db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO books (title, author) VALUES (?, ?)",
            ('Continuous Delivery', 'Dave Farley & Jez Humble')
            )

cur.execute("INSERT INTO books (title, author) VALUES (?, ?)",
            ('CD Pipelines', 'Dave Farley')
            )

cur.execute("INSERT INTO books (title, author) VALUES (?, ?)",
            ('Modern Software Engineering', 'Dave Farley')
            )


connection.commit()
connection.close()