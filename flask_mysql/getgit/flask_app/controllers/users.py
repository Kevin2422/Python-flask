from crypt import methods
from flask_app import app
from flask_app.models.user import User
from flask import render_template,redirect,request,session,flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def homepage():
    
    return render_template('index.html')

