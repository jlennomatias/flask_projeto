import os

SECRET_KEY = 'primeiro_projeto'

SQLALCHEMY_DATABASE_URI = 'postgresql://admin:postgres@0.0.0.0:5432/carteira'

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'