from zlib import decompressobj
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    @classmethod
    def get_all_dojos(cls):
        query = 'SELECT * from dojos;'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    @classmethod
    def create_dojo(cls, data):
        query = 'INSERT INTO dojos (name, created_at, updated_at) VALUES ( %(name)s, NOW(), NOW() );'
        connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def get_ninjas_and_dojos( cls , data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db( query , data )
        print(results)
        # results will be a list of topping objects with the burger attached to each row. 
        dojo = cls( results[0] )
        print(ninja)
        
        for row in results:
            # Now we parse the burger data to make instances of burgers and add them into our list.
            ninja_data = {
                "id" : row["ninjas.id"],
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "age" : row["age"],
                "created_at" : row["ninjas.created_at"],
                "updated_at" : row["ninjas.updated_at"],
                "dojo_id": row['dojo_id']
            }

            print("this is row",row)
            # dojo - line 30 you're making an instance of a Dojo class called 'dojo'
            # ninjas - in your dojo class an empty list
            # ninja - file ninja.py
            # Ninja - class from ninja.py
            #

            dojo.ninjas.append( ninja.Ninja( ninja_data ) ) 
            print('p', dojo)
        return dojo