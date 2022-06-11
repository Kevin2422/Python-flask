from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    dbname = 'recipes'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_created = data['date_created']
        self.under_30 = data['under_30']
        self.user_id = data['user_id']
    @classmethod
    def insert_recipe(cls, data):
        query = 'INSERT INTO recipes (name, description, instructions, date_created, under_30, user_id) VALUES ( %(name)s, %(description)s, %(instructions)s, %(date_created)s, %(under_30)s, %(user_id)s );'
        return connectToMySQL(cls.dbname).query_db(query, data)
    @classmethod
    def get_recipes(cls, data):
        query = 'SELECT * FROM recipes where user_id = %(id)s'
        return connectToMySQL(cls.dbname).query_db(query, data)
    @classmethod
    def get_one_recipe(cls, data):
        query = 'SELECT * FROM recipes where id = %(id)s '
        result = connectToMySQL(cls.dbname).query_db(query, data)
        
        return cls(result[0])
    @classmethod
    def delete_one_recipe(cls, data):
        query = 'Delete FROM recipes where id = %(id)s '
        return connectToMySQL(cls.dbname).query_db(query, data)
    @classmethod
    def update_one_recipe(cls, data):
        query = 'UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_created = %(date_created)s, under_30 = %(under_30)s WHERE id = %(id)s'
        return connectToMySQL(cls.dbname).query_db(query, data)
    @staticmethod
    def validate_user(data):
        is_valid = True
        if not data['name']:
            flash("enter name")
            is_valid = False
        if not data['description']:
            is_valid = False
            flash("enter description")
        if not data['date_created']:
            is_valid = False
            flash("enter date")
        if not data['under_30']:
            is_valid = False
            flash("kughkugk")
        
        
        
        return is_valid