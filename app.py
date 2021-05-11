from flask import Flask, render_template, url_for, json, redirect, request, send_file, flash
import os
from flask_dropzone import Dropzone
from flask_restful import Resource, Api
from gensim.summarization import keywords

# Variable for the root directory of the project 
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

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
    # DROPZONE_REDIRECT_VIEW='completed'
)

# instantiating the drop zone
dropzone = Dropzone(app)

# Route for the home page
@app.route("/", methods=['POST', 'GET'])
def home():

        # Render the template for the home page
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def handle_upload():
    for key, f in request.files.items():
        if key.startswith('file'):
            f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))

    with open('uploads/{}'.format(f.filename)) as f:

        # returning the json object
        rawText = json.load(f)

        # converting to JSON
        jsonString = json.dumps(rawText)

        # Get list of the keyword strings from the JSON
        extractedKeywords = keywords(jsonString)

        # Extracting the lines as separated by \n
        lines = extractedKeywords.split('\n')

        # Instantiating our keyword dictionary
        keywordDict = {
            'keywords': []
        }

        # For each string in our keyword list
        for x in lines:
            
            # append the string to the dictionary as a value in the list corresponding to keywords
            keywordDict['keywords'].append(x)
        
        # Setting up the relative directory
        rel_path = "download/keywords.json"

        # Setting the absolute path variable for the file save location
        abs_path = os.path.join(basedir, rel_path)

        # Writing the keyword Dictionary to a json file in the download directory
        with open(abs_path, 'w') as outfile:
            json.dump(keywordDict, outfile)

    return '', 204

# Route for the page after keyword generation is completed
@app.route("/completed", methods=['GET', 'POST'])
def completed():
                   
    # Return the template for the completed page
    return render_template('completed.html')

# Route for the file download
@app.route("/return_file", methods=['GET'])
def return_file():
    
    # returning the keyword file as a download
    return send_file('download/keywords.json',
                     attachment_filename='keywords.json',
                     as_attachment=True)



# The code below represents the tentative code that will be used to
# pass json through the API to teammates

    # filePath = "download/keywords.json"
    # with open(filePath) as f:
    #     rawText = json.load(f)
        
    # class fileDownload(Resource):

    #     def get(self):
    #         return rawText

    # api.add_resource(fileDownload, '/api')

if __name__ == '__main__':
    app.run(debug=True)

