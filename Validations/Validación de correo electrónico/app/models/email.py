from app.config.mysqlconnection import connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

class Email:
    # using a class variable to hold my database name
    db = "email_validation_schema"
    def __init__(self,data):
        self.id = data.get('id', 0)
        self.email = data.get('email', '')
        self.created_at = data.get('created_at', '')
        self.updated_at = data.get('updated_at', '')

    # class method to save the email object in the data base
    @classmethod
    def save(cls,data):
        query = "INSERT INTO emails (email, created_at) VALUES (%(email)s, NOW());"
        return connectToMySQL(cls.db).query_db(query,data)
    
    # class method to get all the emails fromt the database
    @classmethod
    def get_all(cls):
        query= "SELECT * FROM emails;"
        results = connectToMySQL(cls.db).query_db(query)
        emails = []
        for fila in results:
            emails.append( cls(fila) )
        return emails

    # class method to delete an email from the database based on the PK.
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @staticmethod
    def is_valid(email):
        is_valid = True
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL(Email.db).query_db(query,email)
        if len(results) >= 1:
            flash("Este email esta en uso.", "danger")
            is_valid=False
        if not EMAIL_REGEX.match(email['email']):
            flash("Email Invalido!!!!.", "danger")
            is_valid=False
        return is_valid
    