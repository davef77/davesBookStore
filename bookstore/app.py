from flask import Flask, render_template, request

import booklist
from store import Store

app = Flask(__name__)
bookstore = Store(book_list=booklist)


@app.route('/')
def index():
    return render_template('index.html', books=(bookstore.list_books()))


@app.route('/admin', methods=['POST', 'GET'])
def admin():
    if request.method == 'POST':
        print("admin adding a book")
        bookstore.add_book(request.form['bookTitle'], request.form['bookAuthor'])

    return render_template('admin.html')
