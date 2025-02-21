import os 
from dotenv import load_dotenv 

# loading the environment variables from the .env file 
load_dotenv()


# base configuration class 
class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY", "fallback_key")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# development phase config class extending the base config class 
class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_CONNECTION_STRING","sqlite:///dev.db")


# production phase config class extending the base config class 
class ProdConfig(BaseConfig):
    DEBUG = False 
    SQLALCHEMY_DATABASE_URI = os.getenv("PROD_DB_URL","sqlite:///prod.db")


# testing phase config class extending the base config class 
class TestConfig(BaseConfig):
    TESTING = True 
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DB_URL","sqlite:///test.db")





