from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash

class Painting:
    dbname = 'paintings'
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.price = data['price']
        self.user_id = data['user_id']
        self.name = data['name']
        self.user = {}

    @classmethod
    def add_painting(cls, data):
        query = 'INSERT INTO paintings (user_id, title, description, price, name) VALUES ( %(user_id)s, %(title)s, %(description)s, %(price)s, %(name)s );'
        connectToMySQL(cls.dbname).query_db(query, data)
    @classmethod
    def selectallpaintings(cls):
        query = 'select * from paintings'
        result = connectToMySQL(cls.dbname).query_db(query)
        all_paintings = []
        for row in result:
            all_paintings.append(Painting(row))
        return all_paintings
    @classmethod
    def select_painting(cls, data):
        query = "SELECT * FROM paintings JOIN users ON paintings.user_id = users.id where paintings.id = %(id)s;"
        result = connectToMySQL(cls.dbname).query_db(query, data)
        print ('results', result)
        painting = cls(result[0])
        user_data = {
            'id': result[0]['users.id'],
            'first_name': result[0]['first_name'],
            'last_name': result[0]['last_name'],
            'email': result[0]['email'],
            'password': result[0]['password']
        }
        painting.user = user.User(user_data)
        print(painting)
        return painting
    @classmethod
    def all_painting(cls):
        query = "SELECT * FROM paintings JOIN users ON paintings.user_id = users.id "
        result = connectToMySQL(cls.dbname).query_db(query)
        print ('results', result)
        allpaintings = []
        for x in result:
            painting = cls(x)
            user_data = {
                'id': x['users.id'],
                'first_name': x['first_name'],
                'last_name': x['last_name'],
                'email': x['email'],
                'password': x['password']
            }
            painting.user = user.User(user_data)
            allpaintings.append(painting)
        print(painting)
        return allpaintings
    # @classmethod
    # def select_all_paintings(cls, data):
    #     query = "SELECT * FROM paintings JOIN users ON paintings.user_id = users.id where paintings.id = %(id)s;"
    #     result = connectToMySQL(cls.dbname).query_db(query, data)
    #     print ('results', result)
    #     painting = cls(result[0])
    #     user_data = {
    #         'id': result[0]['users.id'],
    #         'first_name': result[0]['first_name'],
    #         'last_name': result[0]['last_name'],
    #         'email': result[0]['email'],
    #         'password': result[0]['password']
    #     }
    #     painting.user = user.User(user_data)
    #     print(painting)
    #     return painting
    @classmethod
    def update_painting(cls, data):
        query = 'UPDATE paintings SET title = %(title)s, description = %(description)s, price = %(price)s, name = %(name)s WHERE id = %(id)s'
        result = connectToMySQL(cls.dbname).query_db(query, data)
    @classmethod
    def delete_painting(cls,data):
        query = 'DELETE FROM paintings WHERE id = %(id)s'
        result = connectToMySQL(cls.dbname).query_db(query, data)

    @staticmethod
    def validate_painting(data):
        is_valid = True
        if  len(data['title'])<2:
            flash("title too short")
            is_valid = False
        if  len(data['description'])<10:
            is_valid = False
            flash("description too short")
        if  not data['price']:
            is_valid = False
            flash('enter price')
        if data['price'] != '':
            if  int(data['price'])<0:
                is_valid = False
                flash("value is negative")
        
        
        
        
        return is_valid

