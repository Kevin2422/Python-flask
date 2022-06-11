
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_app.models.recipe import Recipe
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    dbname = 'recipes'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['date_created']
        self.updated_at = data['date_updated']
        self.recipes = []
    @classmethod
    def register_user(cls, data):
        query = 'INSERT INTO Users (first_name, last_name, email, password, date_created, date_updated) VALUES ( %(fname)s, %(lname)s, %(email)s, %(phash)s, NOW(), NOW() );'
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
    def get_users_and_recipes( cls , data ):
        query = "SELECT * FROM users LEFT JOIN recipes ON recipes.user_id = users.id WHERE users.id = %(id)s;"
        results = connectToMySQL(cls.dbname).query_db( query , data )
        print(results)
        # results will be a list of topping objects with the burger attached to each row. 
        user1 = cls( results[0] )
        if results[0]['description'] == None:
            return False
        print(user1)
        
        for row in results:
            # Now we parse the burger data to make instances of burgers and add them into our list.
            recipe_data = {
                "id" : row["recipes.id"],
                "description" : row["description"],
                "under_30" : row["under_30"],
                "instructions" : row["instructions"],
                "date_created" : row["recipes.date_created"],
                'name': row['name'],
                "user_id": row['user_id']
            }

            print("this is row",row)
            # dojo - line 30 you're making an instance of a Dojo class called 'dojo'
            # ninjas - in your dojo class an empty list
            # ninja - file ninja.py
            # Ninja - class from ninja.py
            #

            user1.recipes.append(Recipe( recipe_data ) ) 
            print('p', user1)
        return user1
    # @classmethod
    # def send_message(cls,data):
    #     query = 'INSERT INTO messages (name, user_id, content, date_sent) VALUES ( %(name)s, %(user_id)s, %(content)s,  NOW());'
    #     connectToMySQL(cls.dbname).query_db(query, data)
    # @classmethod
    # def receive_message(cls,data):
    #     query = 'SELECT * FROM messages WHERE user_id = %(id)s'
    #     return connectToMySQL(cls.dbname).query_db(query, data)
    # @classmethod
    # def delete_messages(cls,data):
    #     query = 'DELETE FROM messages WHERE user_id = %(id)s and date_sent = %(date_sent)s'
    # #     return connectToMySQL(cls.dbname).query_db(query, data)
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