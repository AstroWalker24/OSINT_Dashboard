import os
from config.config import DevConfig, ProdConfig, TestConfig



env = os.getenv("FLASK_ENV", "development")


# setting the configuration dynamically based on the environment 
if env == "production":
    config = ProdConfig

elif env == "testing":
    config = TestConfig

else:
    config = DevConfig

    