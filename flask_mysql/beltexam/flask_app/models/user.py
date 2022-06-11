

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import painting
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    dbname = 'paintings'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.paintings = []
        
    @classmethod
    def register_user(cls, data):
        query = 'INSERT INTO Users (first_name, last_name, email, password) VALUES ( %(fname)s, %(lname)s, %(email)s, %(phash)s );'
        connectToMySQL(cls.dbname).query_db(query, data)
        
    @classmethod
    def get_by_email(cls, data):
        query = 'SELECT * FROM Users WHERE email = %(email)s'
        result = connectToMySQL(cls.dbname).query_db(query, data)
        if len(result)<1:
            return False
        return cls(result[0])
    @classmethod
    def get_everbody_else(cls, data):
        query = 'SELECT * FROM users WHERE NOT email = %(email)s'
        result = connectToMySQL(cls.dbname).query_db(query, data)
        return result
    @classmethod
    def email_exists(cls, data):
        query = 'SELECT * FROM Users WHERE email = %(email)s'
        result = connectToMySQL(cls.dbname).query_db(query, data)
        if len(result)>0:
            return False
        return True
    @classmethod
    def get_users_and_painting( cls , data ):
        query = "SELECT * FROM users JOIN paintings ON paintings.user_id = users.id;"
        results = connectToMySQL(cls.dbname).query_db( query , data )
        print(results[0])
        print(results[0]['description'] )
        # results will be a list of topping objects with the burger attached to each x. 
        if results[0]['description'] == None:
            return False
        all_users = []
        for x in results:
            user1 = cls( x )
            print('user1', user1)
            all_users.append(user1)
            print('all users', all_users)
            painting_data = {
        'id' : x['paintings.id'],
        'title' : x['title'],
        'description' : x['description'],
        'price' : x['price'],
        'user_id' : x['user_id'],
        'name' : x['name']
            }

        

            print("this is x",x)
            # dojo - line 30 you're making an instance of a Dojo class called 'dojo'
            # ninjas - in your dojo class an empty list
            # ninja - file ninja.py
            # Ninja - class from ninja.py
            #

            user1.paintings.append(painting.Painting( painting_data ) ) 
            print('p', user1)
        return all_users

    @staticmethod
    def validate_user(data):
        is_valid = True
        if len(data['fname']) < 3:
            flash("First name must be at least 3 characters")
            is_valid = False
        if len(data['lname']) < 3:
            is_valid = False
            flash("Last name must be at least 3 characters")
        if len(data['password']) < 8:
            is_valid = False
            flash("Password must be at least 8 characters")
        if not data['password'] == data['c_password']:
            is_valid = False
            flash("Please confirm passwords match")
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False
        if not User.email_exists(data):
            flash('email already taken')
            is_valid = False
        
        
        return is_valid