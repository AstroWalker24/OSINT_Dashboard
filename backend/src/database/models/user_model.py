from database import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)


    # this is for OAuth users 
    google_id = db.Column(db.String(255),unique = True, nullable = True)

    # common fields for all users 
    name = db.Column(db.String(100),nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    profile_pic = db.Column(db.String(255))

    # normal authentication users 
    password_hash = db.Column(db.String(255),nullable = False, default = "")


    created_at = db.Column(db.DateTime, default = datetime.now(datetime.timezone.utc))
    role = db.Column(db.String(50),default = "user")


    def set_password(self,password):

        if not password:
            raise ValueError("Password can't be empty!")

        self.password_hash = generate_password_hash(password,method="scrypt",salt_length=16)


    def check_password(self,password):
        if not self.password_hash:
            raise False
        
        return check_password_hash(self.password_hash,password)


    def __repr__(self):
        return f"ID : {self.id} | Name: {self.name} | Email: {self.email} | Role: {self.role}"






    