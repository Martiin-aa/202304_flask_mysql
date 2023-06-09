from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data.get('id', 0)
        self.nombre = data['nombre']
        self.created_at = data.get('created_at', '')
        self.updated_at = data.get('updated_at', '')
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        result = connectToMySQL('dojos_y_ninjas_schema').query_db(query)
        dojos= []
        for x in result:
            dojos.append(cls(x))
        return dojos
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL('dojos_y_ninjas_schema').query_db(query, data)
        return cls(result[0])

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO dojos (nombre, created_at, updated_at) 
        VALUES (%(nombre)s, NOW(), NOW());
        """
        result = connectToMySQL('dojos_y_ninjas_schema').query_db(query, data)
        return result
    
    @classmethod
    def get_ninja_from_dojos(cls, data):
        query = """
        SELECT * FROM dojos INNER JOIN ninjas 
        ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;
        """
        result = connectToMySQL('dojos_y_ninjas_schema').query_db(query, data)
        dojo = cls(result[0])
        for fila in result:
            ninja_data = {
                "id" : fila["ninjas.id"],
                "nombre" : fila["ninjas.nombre"],
                "apellido" : fila["apellido"],
                "edad" : fila["edad"],
                "dojo_id" : fila["dojo_id"],
                "created_at" : fila["ninjas.created_at"],
                "updated_at" : fila["ninjas.updated_at"]
            }
            dojo.ninjas.append(Ninja(ninja_data))
        return dojo
