from flask import Flask
from .src.config import config 
from .src.database import db


app = Flask(__name__)

# configuring the app with the configuration settings from the config module 
app.config.from_object(config)

# initializing the ORM with the app
db.init_app(app)



if __name__=="__main__":
    app.run(debug=True)


    