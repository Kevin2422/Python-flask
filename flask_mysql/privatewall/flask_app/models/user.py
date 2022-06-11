from xmlrpc.server import SimpleXMLRPCRequestHandler
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
    
    @classmethod
    def register_user(cls, data):
        query = 'INSERT INTO Users (first_name, last_name, email, password) VALUES ( %(fname)s, %(lname)s, %(email)s, %(phash)s );'
        connectToMySQL('private_wall').query_db(query, data)
    @classmethod
    def get_by_email(cls, data):
        query = 'SELECT * FROM Users WHERE email = %(email)s'
        result = connectToMySQL('private_wall').query_db(query, data)
        if len(result)<1:
            return False
        return cls(result[0])
    @classmethod
    def get_everbody_else(cls, data):
        query = 'SELECT * FROM users WHERE NOT email = %(email)s'
        result = connectToMySQL('private_wall').query_db(query, data)
        return result
    @classmethod
    def email_exists(cls, data):
        query = 'SELECT * FROM Users WHERE email = %(email)s'
        result = connectToMySQL('private_wall').query_db(query, data)
        if len(result)>0:
            return False
        return True
    @classmethod
    def send_message(cls,data):
        query = 'INSERT INTO messages (name, user_id, content, date_sent) VALUES ( %(name)s, %(user_id)s, %(content)s,  NOW());'
        connectToMySQL('private_wall').query_db(query, data)
    @classmethod
    def receive_message(cls,data):
        query = 'SELECT * FROM messages WHERE user_id = %(id)s'
        return connectToMySQL('private_wall').query_db(query, data)
    @classmethod
    def delete_messages(cls,data):
        query = 'DELETE FROM messages WHERE user_id = %(id)s and date_sent = %(date_sent)s'
        return connectToMySQL('private_wall').query_db(query, data)
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