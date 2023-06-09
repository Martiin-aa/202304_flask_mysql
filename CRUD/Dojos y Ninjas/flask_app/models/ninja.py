from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self , data):
        self.id = data.get('id', 0)
        self.nombre = data.get('nombre', '')
        self.apellido = data.get('apellido', '')
        self.edad = data.get('edad', '')
        self.dojo_id = data.get('dojo_id', '')
        self.created_at = data.get('created_at', '')
        self.updated_at = data.get('updated_at', '')

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO ninjas (nombre, apellido, edad, dojo_id, created_at , updated_at) 
        VALUES (%(nombre)s, %(apellido)s, %(edad)s, %(dojo_id)s, NOW(), NOW());
        """
        result = connectToMySQL('dojos_y_ninjas_schema').query_db(query, data)
        return result
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL('dojos_y_ninjas_schema').query_db(query, data)
        return cls(result[0])
