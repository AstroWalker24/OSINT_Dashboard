from flask import Blueprint, redirect, url_for, request, jsonify
from src.config.config import BaseConfig
from authlib.integrations.flask_client import OAuth
from src.database.models.user_model import User
from src.database import db
import jwt
import os
import datetime
import requests


# creating an instance of the auth blueprint 
auth_bp = Blueprint("auth",__name__)

# creating an instance of OAuth class
oauth = OAuth()
oauth.init_app(None)


# registering the google oauth provider with OAuth instance 
google_oauth = oauth.register(
    name = "google",
    client_id = BaseConfig.GOOGLE_CLIENT_ID,
    client_secret = BaseConfig.GOOGLE_CLIENT_SECRET,
    access_token_url = "https://oauth2.googleapis.com/token",
    authorize_url = "https://accounts.google.com/o/oauth2/auth",
    client_kwargs = {"scope": "openid profile email"}
)


@auth_bp.route("/register",methods=["POST"])
def register():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    # validate the request data 
    if not name or not email or not password:
        return jsonify({"error":"Name, Email and password are required fields"}),400
    
    # check for the exisiting user with the same email
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"error":"User with this email already exists"}),400
    

    # create a new user 
    user = User(name=name,email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()


    return jsonify({"message":"User created successfully"}),201
    


@auth_bp.route("/login")
def login():
    return google_oauth.authorize_redirect(BaseConfig.OAUTH_REDIRECT_URI) 

@auth_bp.route("/auth/callback")
def auth_callback():
    token = google_oauth.authorize_access_token()
    user = google_oauth.parse_id_token(token)





