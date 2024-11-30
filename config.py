import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class Config:
    API_TITLE = "RESTAURANT API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'mysql://monette:monette_08202003@monette.mysql.pythonanywhere-services.com/monette$keriderya_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    # SSL settings passed as 'connect_args'
