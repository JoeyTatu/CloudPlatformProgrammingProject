import os

from flask import Flask, render_template, request, redirect, send_file, url_for

from s3 import list_files, get_image, upload_file

import logging
import boto3
from botocore.exceptions import ClientError
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import io


app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
BUCKET = "cpp-project-jtatu"

@app.route('/')
def entry_point():
    return 'Hello World!'


@app.route("/storage")
def storage():
    contents = list_files("cpp-project-jtatu")
    return render_template('storage.html', contents=contents)


@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']
        f.save(f.filename)
        upload_file(f"{f.filename}", BUCKET)

        return redirect("/storage")
  
@app.route("/temp/<filename>")        
def temp(filename):
    response = get_image(BUCKET, filename)

    return render_template('temp.html', respone=response)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8080, debug=True)
