from flask import Flask, render_template, url_for, json, redirect, request
# from forms import keywordForm
import pandas as pd 
import os
from flask_dropzone import Dropzone

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.update(

    # Configuring drop zone. Upload path is a dir called uploads, max file size 1gb, max timeout 3 mins, only allowing json files

    UPLOAD_PATH = os.path.join(basedir,'uploads'),
    DROPZONE_MAX_FILE_SIZE = 1024,
    DROPZONE_TIMEOUT = 3*60*1000,
    DROPZONE_ALLOWED_FILE_CUSTOM = True,
    DROPZONE_ALLOWED_FILE_TYPE = '.json',
    DROPZONE_MAX_FILES = 1 
)

dropzone = Dropzone(app)

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():

    # The flask dropzone POST code was borrowed from the documentation https://flask-dropzone.readthedocs.io/en/latest/basic.html
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join(app.config['UPLOAD_PATH'], f.filename))

    return render_template('home.html')