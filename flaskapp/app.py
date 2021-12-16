import os

from flask import Flask, render_template, request, redirect, send_file, url_for, jsonify
# from flask_sqlalchemy import SQLAlchemy
import aws_controller

from s3

import logging
import boto3
from botocore.exceptions import ClientError
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import io


app = Flask(__name__)

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

### Home
@app.route('/') # Home page
def entry_point():
    return render_template('index.html')
    
## DynamoDB
@app.route('/get-items')
def get_items():
    return jsonify(aws_controller.get_items())

### Account    
@app.route("/account")
def account():
    return "Accounts Index"
    
@app.route('/account/profile')
def profile():
    return render_template('account/profile.html')
    
@app.route("/account/signup")
def sign_up():
    return "Account/SignUp"

@app.route("/account/login")
def login():
    return "Account/Login"
    
@app.route("/account/logout")
def logout():
    return "Account/Logout"
    
@app.route("/account/access/<action>") #action = "login" or "signup"
def access(action):
    action = ""
    return "/account/access/<action>"
    
### Images
@app.route("/image") # Storage page to upload and store images. 
def storage():
    contents = list_files("cpp-project-jtatu")
    return render_template('image/index.html', contents=contents)


@app.route("/image/upload", methods=['POST']) # Uploaded files get sent to /upload to be uploaded to S3
def upload():
    if request.method == "POST":
        f = request.files['file']
        f.save(f.filename)
        upload_file(f"{f.filename}", BUCKET)

        return redirect("/image")
        
@app.route("/image/download/<filename>", methods=['GET'])
def download(filename):
    if request.method == 'GET':
        output = download_file(filename, BUCKET)

        return send_file(output, as_attachment=True)
        
@app.route("/image/scan")
def scan_image():
    return "Image/Scan"
    
@app.route("/image/scan_result")
def scan_result():
    return "Image/scan_result"
    

### Twitter
@app.route("/twitter")
def twitter():
    return "Twitter"
    
@app.route("/twitter/search")
def search():
    return "Twitter/Search"
    
@app.route("/twitter/search_result")
def result():
    return "Twitter/search_result"
    

# ### Temp  
# @app.route("/temp/<filename>") # This was planned to show an image when the user clicked on it. But the response cannot be an image.
# def temp(filename):
#     response = get_image(BUCKET, filename)

#     return render_template('temp.html', respone=response)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8080, debug=True)
