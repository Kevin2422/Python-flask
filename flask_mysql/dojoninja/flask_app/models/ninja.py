from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
        
    @classmethod
    def insert_ninja(cls,data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at,dojo_id) VALUES (%(fname)s, %(lname)s, %(age)s, NOW(), NOW(), %(dojo_id)s);'
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )

      
    # @classmethod
    # def get_ninjas_and_dojos( cls , data ):
    #     query = "SELECT * FROM ninjas LEFT JOIN dojos ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
    #     results = connectToMySQL('dojos_and_ninjas_schema').query_db( query , data )
    #     print(results)
    #     # results will be a list of topping objects with the burger attached to each row. 
    #     ninja = cls( results[0] )
    #     print(ninja)
        
    #     for row in results:
    #         # Now we parse the burger data to make instances of burgers and add them into our list.
    #         ninja_data = {
    #             "id" : row["ninjas.id"],
    #             "first_name" : row["ninjas.first_name"],
    #             "last_name" : row["ninjas.last_name"],
    #             "age" : row["ninjas.age"],
    #             "created_at" : row["ninjas.created_at"],
    #             "updated_at" : row["ninjas.updated_at"]
    #         }
    #         restaurant.burgers.append( burger.Burger( ninja_data ) )
    #     return restaurant
    
    @staticmethod
    def validate_ninja(data):
        is_valid = True # we assume this is true
        if len(data['fname']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(data['lname']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        
        return is_valid


