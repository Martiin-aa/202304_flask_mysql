from app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    def __init__(self,data):
        self.id = data.get('id', 0)
        self.name = data.get('name', '')
        self.location = data.get('location', '')
        self.language = data.get('language', '')
        self.comments = data.get('comments', '')
        self.created_at = data.get('created_at', '')
        self.updated_at = data.get('updated_at', '')

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM surveys;"
        result = connectToMySQL('dojo_survey_schema').query_db(query)
        surveys = []
        for x in result:
            surveys.append(cls(x))
        return surveys
    
    @classmethod
    def save(cls, data):
        query = """
        INSERT into surveys (name,location,language,comments,created_at,updated_at) 
        VALUES (%(name)s,%(location)s,%(language)s,%(comments)s,NOW(),NOW());
        """
        return connectToMySQL('dojo_survey_schema').query_db(query,data)

    @classmethod
    def get_last_survey(cls):
        query = "SELECT * FROM surveys ORDER BY surveys.id DESC LIMIT 1;"
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        return Survey(results[0])

    @staticmethod
    def is_valid(survey):
        is_valid = True
        if len(survey['name']) < 3:
            is_valid = False
            flash("El nombre debe tener al menos 3 caracteres.", "danger")
        if len(survey['location']) < 1:
            is_valid = False
            flash("Debes escoger una ubicacion del dojo.", "danger")
        if len(survey['language']) < 1:
            is_valid = False
            flash("Debes escoger un idioma.", "danger")
        if len(survey['comments']) < 3:
            is_valid = False
            flash("El comentario debe de tener al menos 3 caracteres.", "danger")
        return is_valid
    