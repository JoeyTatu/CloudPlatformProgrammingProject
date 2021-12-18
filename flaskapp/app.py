import os, logging, boto3, io
import matplotlib.pyplot as plt, matplotlib.image as mpimg, numpy as np
import auth
import aws_controller

# from apps.User.models import db
from flask import Flask, render_template, request, redirect, send_file, url_for, jsonify, Blueprint
from flask_bootstrap import Bootstrap
from connection import list_files, upload_file, download_file, scan_image, search_tweets, show_image
from botocore.exceptions import ClientError
from flask_sqlalchemy import SQLAlchemy


main = Blueprint('main', __name__)
app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
BUCKET = "cpp-project-jtatu"
bootstrap = Bootstrap(app)

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "397a0f7bb048488fa34ac741d118a9c0"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    
    db.init_app(app)

    # blueprint for auth routes in our app
    # import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint)

    # # blueprint for non-auth parts of app
    # from .main import main as main_blueprint
    # app.register_blueprint(main_blueprint)

    return app

### Home
@app.route('/') # Home page
def index():
    contents = list_files(BUCKET)
    return render_template('image/index.html', contents=contents)
    
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
def signup():
    return render_template('account/signup.html')

@app.route("/account/login")
def login():
    return render_template('account/login.html')
    
@app.route("/account/logout")
def logout():
    contents = list_files(BUCKET)
    return render_template('image/index.html', contents=contents)
    
@app.route("/account/access/<action>") #action = "login" or "signup"
def access(action):
    action = ""
    return "/account/access/<action>"
    
### Images
@app.route("/image")
@app.route('/')# Storage page to upload and store images. 
def storage():
    contents = list_files(BUCKET)
    # contents = show_image(BUCKET)
    return render_template('image/index.html', contents=contents)

@app.route('/upload', methods=['POST'])
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
        
@app.route("/image/scan/<filename>", methods=['GET'])
def scan(filename):
    if request.method == 'GET':
        response = {}
        response = scan_image(BUCKET, filename)
        
        return render_template('image/scan_result.html', response=response)
    # return "Image/Scan"
    
@app.route("/image/scan_result")
def scan_result():
    return "Image/scan_result"
    

### Twitter

    
@app.route("/search/<query>", methods=['GET'])
def search(query):
    
    response = {}
    api = search_tweets(query)
    
    return "Twitter/Search"
    
@app.route("/search_result")
def result():
    return "Twitter/search_result"
    

# ### Temp  
# @app.route("/temp/<filename>") # This was planned to show an image when the user clicked on it. But the response cannot be an image.
# def temp(filename):
#     response = get_image(BUCKET, filename)

#     return render_template('temp.html', respone=response)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8080, debug=True)
