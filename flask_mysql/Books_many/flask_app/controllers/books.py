from flask_app import app
from flask import render_template, session, redirect, request
from flask_app.models.book import Book


@app.route('/create/')
def display_book_page():
    all_books = Book.get_all_books()
    return render_template('addbook.html', all_books = all_books)

@app.route('/addbook/', methods=["post"])
def new_book():
    data = {
        "title" : request.form["title"],
        "num_of_pages" : request.form["num_of_pages"]
    }
    Book.add_book(data)
    return redirect("/")
