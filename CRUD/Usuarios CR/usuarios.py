from mysqlconnection import connectToMySQL

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
        query = "SELECT id, nombre, apellido, email, created_at FROM usuarios;"
        result = connectToMySQL('users_schema').query_db(query);
        usuarios= []
        for x in result:
            usuarios.append(cls(x))
        return usuarios

    @classmethod
    def save(self, data):
        query = "INSERT INTO usuarios (nombre, apellido, email, created_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, NOW());"
        result = connectToMySQL('users_schema').query_db(query, data)
        return result
