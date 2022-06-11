from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
class Book:
    dbname = 'books/users'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.author = data['author']
        self.users = []
    @classmethod
    def get_books_with_users( cls , data ):
        query = "SELECT * FROM books LEFT JOIN books_has_users ON books_has_users.book_id = books.id LEFT JOIN users ON books_has_users.user_id = users.id WHERE books.id = %(id)s;"
        results = connectToMySQL(cls.dbname).query_db( query , data )
        # results will be a list of topping objects with the burger attached to each row. 
        book = cls( results[0] )
        for row in results:
        # Now we parse the topping data to make instances of users and add them into our list.
            book_data =  {
            'id' : row['id'],
            'first_name' : row['first_name'],
            'last_name' : row['last_name'],
            'email' : row['email'],
            'password' : row['password'],
            'date_created' : row['date_created'],
            'date_updated' : row['date_updated']
                }
            book.users.append( user.User( book_data ) )
        return book
    @classmethod
    def add_book(cls, data):
        query = "Insert into books (name, author) values (%(name)s, %(author)s)"
        results = connectToMySQL(cls.dbname).query_db( query , data )
        return results
    @classmethod
    def showbooks(cls):
        query = 'select * from books'
        results = connectToMySQL(cls.dbname).query_db( query)
        allbook = []
        for row in results:
            book_data =  {
                'id' : row['id'],
                'name' :  row['name'],
                'author' :  row['author']
                }
            results=     allbook.append(Book(book_data))
            
        return allbook