import re
import os
from app.config.mysqlconnection import connectToMySQL
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Usuario:
    def __init__(self, data):
        self.id = data.get('id', 0)
        self.email = data['email']
        self.password = data['password']
        self.created_at = data.get('created_at', '')
        self.updated_at = data.get('updated_at', '')
    
    @classmethod
    def get_all(cls):
        query= "SELECT * FROM usuarios;"
        results = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(query)
        usuarios = []
        for fila in results:
            usuarios.append( cls(fila) )
        return usuarios

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @classmethod
    def save(cls,data):
        query = """
        INSERT INTO usuarios (email, password, created_at, updated_at) 
        VALUES (%(email)s,%(password)s, NOW(), NOW());
        """
        return connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = """
        UPDATE usuarios SET email=%(email)s, password=%(password)s, updated_at=NOW() 
        WHERE id = %(id)s;
        """
        return connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM usuarios WHERE id = %(id)s;"
        return connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(query,data)

    @staticmethod
    def validate_register(usuario):
        is_valid = True
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        results = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(query, usuario)
        if len(results) >= 1:
            flash("Email ocupado.","danger")
            is_valid=False
        if not EMAIL_REGEX.match(usuario['email']):
            flash("Email invalido!!!","danger")
            is_valid=False
        if len(usuario['password']) < 8:
            flash("La contraseña debe tener al menos 8 caracteres","danger")
            is_valid= False
        if usuario['password'] != usuario['confirm_password']:
            flash("Las contraseñas no coinciden","danger")
        return is_valid
