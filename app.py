from flask import Flask, render_template, url_for, json, redirect, request, send_file, flash
import os
import requests
from flask_dropzone import Dropzone
from flask_restful import Resource, Api, reqparse, abort
from keywordGenerator import generateKeywords_from_file, generateKeywords_from_api

# Variable for the root directory of the project 
basedir = os.path.abspath(os.path.dirname(__file__))

# instantiating the app
app = Flask(__name__)

# Instantiating the API
api = Api(app)

# Configuring drop zone
app.config.update(
    UPLOADED_PATH = os.path.join(basedir,'uploads'),
    DROPZONE_MAX_FILE_SIZE = 1024,
    DROPZONE_TIMEOUT = 3*60*1000,
    DROPZONE_ALLOWED_FILE_CUSTOM = True,
    DROPZONE_ALLOWED_FILE_TYPE = '.json',
    DROPZONE_MAX_FILES = 1,
    DROPZONE_INVALID_FILE_TYPE = "INVALID FILE TYPE: Please upload a .json file",
    DROPZONE_UPLOAD_ON_CLICK = True,
    DROPZONE_IN_FORM=True,
    DROPZONE_UPLOAD_ACTION='handle_upload',  # URL or endpoint
    DROPZONE_UPLOAD_BTN_ID='upload'
)

# instantiating the drop zone
dropzone = Dropzone(app)

put_keywordList = {}

# --------------------------------------------------------------------------
# The code below is for users to pass data to the app in a post request and 
# get the keyword list generated from their text
# --------------------------------------------------------------------------
class keywordUpload(Resource):
    def get(self):

        # If the keyword list isn't empty, return it
        if put_keywordList:
            return put_keywordList["keywords"]
        else:
            return "There are no values in the keyword list!"

    def post(self):

        # get the json data and store in a temp dict
        tempDict = request.get_json(force=True)

        # # convert the dict to a json string
        jsonString = json.dumps(tempDict)

        # Use global variable
        global put_keywordList

        # call helper function with the json string
        put_keywordList = json.loads(generateKeywords_from_api(jsonString))

        return '', 202

# ------------------------------------------------------------------------
# The code below is used to pass json through the API to teammates
# ------------------------------------------------------------------------
class Keyword(Resource):
    def get(self):

        # GET VALERIES DATA as JSON
        val_url = "http://valchin.com/sendjson2021"
        response = requests.get(val_url)
        
        # Use response.json to change to a dict
        tempDict = response.json()

        # Convert to a json string
        jsonString = json.dumps(tempDict)

        # Call the helper function with the json String
        keywordList = generateKeywords_from_api(jsonString)

        return keywordList


# ------------------------------------------------------------------------
# The code below is the routing for the web pages
# ------------------------------------------------------------------------
@app.route("/", methods=['POST', 'GET'])
def home():

    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def handle_upload():
    for key, f in request.files.items():
        if key.startswith('file'):
            f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))

    # Generate the keywords and save to the downloads file
    generateKeywords_from_file('uploads/{}'.format(f.filename))

    return '', 204

@app.route("/completed", methods=['GET', 'POST'])
def completed():
                   
    return render_template('completed.html')

@app.route("/return_file", methods=['GET'])
def return_file():
    
    return send_file('download/keywords.json',
                     attachment_filename='keywords.json',
                     as_attachment=True)

api.add_resource(Keyword, "/keyword")
api.add_resource(keywordUpload, "/keywordUpload")

if __name__ == '__main__':
    app.run(debug=True)

