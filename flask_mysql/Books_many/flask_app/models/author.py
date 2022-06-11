from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author: 
    def __init__ ( self, data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.books = []

    @classmethod
    def add_author(cls, data):
        query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, now(), now());"
        return connectToMySQL('books_fav_schema').query_db(query, data)

    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors"
        results = connectToMySQL('books_fav_schema').query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors
    
    @classmethod
    def one_author_info(cls, data):
        query = "SELECT * FROM authors WHERE id = %(id)s;"
        results = connectToMySQL('books_fav_schema').query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_author_favorite(cls, data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books_fav_schema').query_db(query, data)

        author= cls(results[0])
        
        for row_from_db in results:
            book_data = {
                "id" : row_from_db["books.id"],
                "title" : row_from_db["title"],
                "num_of_pages" : row_from_db["num_of_pages"],
                "created_at" : row_from_db["created_at"],
                "updated_at" : row_from_db["updated_at"]
            }
            author.books.append(book.Book(book_data))
        return author


