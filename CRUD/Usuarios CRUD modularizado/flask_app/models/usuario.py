from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data.get('id', 0)
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.created_at = data.get('created_at', '')
        self.updated_at = data.get('updated_at', '')

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        result = connectToMySQL('users_schema').query_db(query);
        usuarios= []
        for x in result:
            usuarios.append(cls(x))
        return usuarios
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        result = connectToMySQL('users_schema').query_db(query, data);
        return cls(result[0])

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO usuarios (nombre, apellido, email, created_at, updated_at) 
        VALUES (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());
        """
        result = connectToMySQL('users_schema').query_db(query, data)
        return result

    @classmethod
    def update(cls, data):
        query = """
        UPDATE usuarios SET nombre=%(nombre)s, apellido=%(apellido)s, email=%(email)s, updated_at=NOW() 
        WHERE id = %(id)s;
        """
        return connectToMySQL('users_schema').query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM usuarios WHERE id = %(id)s"
        return connectToMySQL('users_schema').query_db(query, data)
