from flask import Flask, render_template, request

import booklist
import db
from store import Store

db.init_db()
app = Flask(__name__)
bookstore = Store(book_list=booklist)


@app.route('/')
def index():
    return render_template('index.html', books=(bookstore.list_books()))


@app.route('/admin', methods=['POST', 'GET'])
def admin():
    if request.method == 'POST':
        bookstore.add_book(request.form['bookTitle'], request.form['bookAuthor'])

    return render_template('admin.html')
