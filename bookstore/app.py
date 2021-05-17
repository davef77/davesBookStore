from flask import Flask, render_template

import booklist
from store import Store

app = Flask(__name__)
store = Store(book_list=booklist)

@app.route('/')
def index():
    return render_template('index.html', books=(store.list_books()))
