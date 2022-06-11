from flask_app import app
from flask import render_template, session, redirect, request
from flask_app.models.author import Author
from flask_app.models.book import Book


@app.route('/')
def index():
    all_authors = Author.get_all_authors()
    return render_template('index.html', all_authors = all_authors)

@app.route('/addauthor/', methods=["post"])
def new_author():
    data = {
        "name" : request.form["name"]
    }
    Author.add_author(data)
    return redirect("/")

@app.route('/authors/<int:author_id>/')
def show_one_author(author_id):
    author_data = {
        "id" : author_id 
    }
    author_info= Author.one_author_info(author_data)

    all_favorites = Author.get_author_favorite(author_data)

    all_books = Book.get_all_books()

    return render_template("author_show.html", all_books = all_books, all_favorites = all_favorites, author_info = author_info)

@app.route('/addfavorite/', methods=["post"])
def add_favorite_book():
    data = {
        "author_id" : request.form["author_id"],
        "book_id" : request.form["book_id"]
    }
    Book.add_to_favorites(data)
    return redirect(f"/authors/{request.form['author_id']}/")



