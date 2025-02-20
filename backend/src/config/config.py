import os 
from dotenv import load_dotenv 

# loading the environment variables from the .env file 
load_dotenv()



class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY", "fallback_key")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DEV_DB_URL","sqlite:///dev.db")

class ProdConfig(BaseConfig):
    DEBUG = False 
    SQLALCHEMY_DATABASE_URI = os.getenv("PROD_DB_URL","sqlite:///prod.db")


class TestConfig(BaseConfig):
    TESTING = True 
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DB_URL","sqlite:///test.db")





