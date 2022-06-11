from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models.author import Author

class Book: 
    def __init__ ( self, data ):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_book(cls, data):
        query = "INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES (%(title)s, %(num_of_pages)s, now(), now());"
        return connectToMySQL('books_fav_schema').query_db(query, data)

    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books"
        results = connectToMySQL('books_fav_schema').query_db(query)
        books = []
        for book in results:
            books.append(cls(book))
        return books

    @classmethod
    def add_to_favorites(cls, data):
        query = "INSERT INTO favorites (book_id, author_id) VALUEs (%(book_id)s, %(author_id)s);"
        return connectToMySQL('books_fav_schema').query_db(query, data)
