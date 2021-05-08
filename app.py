from flask import Flask, render_template, url_for, json, redirect, request
# from forms import keywordForm
import pandas as pd 
import os
from flask_dropzone import Dropzone
from gensim.summarization import keywords

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Configuring drop zone. Upload path is a dir called uploads, max file size 1gb, max timeout 3 mins, only allowing json files
app.config.update(
    UPLOADED_PATH = os.path.join(basedir,'uploads'),
    DROPZONE_MAX_FILE_SIZE = 1024,
    DROPZONE_TIMEOUT = 3*60*1000,
    DROPZONE_ALLOWED_FILE_CUSTOM = True,
    DROPZONE_ALLOWED_FILE_TYPE = '.json',
    DROPZONE_MAX_FILES = 1
)

dropzone = Dropzone(app)

@app.route("/", methods=['POST', 'GET'])
def upload():

    # The flask dropzone code was borrowed from the documentation https://flask-dropzone.readthedocs.io/en/latest/basic.html
    if request.method == 'POST':
        for key, f in request.files.items():
            if key.startswith('file'):
                f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
                print(f)

        with open('uploads/{}'.format(f.filename)) as f:
         rawText = json.load(f)

        jsonString = json.dumps(rawText)

        print(keywords(jsonString))


        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

