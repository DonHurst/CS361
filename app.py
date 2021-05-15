from flask import Flask, render_template, url_for, json, redirect, request, send_file, flash
import os
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

# Keyword API stuff - put arguments
keyword_put_args = reqparse.RequestParser()
keyword_put_args.add_argument("id", type=int, help="Keyword_id_number", required=True)
keyword_put_args.add_argument("title", type=str, help="Title of game", required=True)
keyword_put_args.add_argument("jsonString", type=str, help="Scraped text", required=True)

# Dictionary containing all of the passed-in information
keywords = {}

# Dictionary containing all of the keyword values
keyword_list = {0: {'id': 0, 'title': 'pokemon Snap', 'jsonString': ["gaming", "pok", "video game", "console games", "editor", "editors", "calling", "nintendo", "ign", "sequel called", "commented", "commenting", "commentators", "released", "release", "snap", "author", "players", "player", "videos", "including", "includes", "included", "include", "series", "titles", "new", "news", "featuring", "featured", "feature", "pictures", "picture", "best", "title development", "time", "times", "like", "better", "version features", "praised", "praising", "originally", "developer", "life", "magazine", "taking", "scoring", "scores", "takes photographs", "photographer", "photographing", "photographic", "later", "retronauts", "posted", "post", "gameplay mechanics developed", "appearance", "appearing", "states", "stating", "stated", "accessories", "accessory", "earthbound", "photos", "photo", "initially", "initial", "designers", "design", "adventure", "adventures", "original generation", "todd", "end", "ending", "printed", "print", "blockbuster", "levels", "level", "fun", "wii", "oak", "fairy", "good", "promoted", "promotions", "storage", "regions", "gran", "clank", "elements ended", "japan", "little", "special", "briefly appeared", "sold", "book", "pikachu", "different", "songs", "card", "cards", "wired", "steel", "prowess citing", "dead", "general", "generally", "generations", "justin", "positive reception", "similar", "person", "personal", "received", "fantasy", "mark", "world", "cave", "entertaining", "amphibious", "freak", "united", "units", "rainbow", "having", "podcast", "quality", "feel", "feeling", "based", "virtual", "mechanic", "professor", "japanese", "viii", "discussed", "training", "diversion", "pokemon", "river"]}}

# function to abort if no id is passed
def abort_if_no_keyword_id(keyword_id):
    if keyword_id not in keywords:
        abort(404, message="Keyword Id is not valid...")

# The code below represents the tentative code that will be used to
# pass json through the API to teammates
# ------------------------------------------------------------------------

class Keyword(Resource):
    def get(self, keyword_id):
        # abort_if_no_keyword_id(keyword_id)
        # print(keyword_id)
        return keyword_list[keyword_id]

    def put(self, keyword_id):
        args = keyword_put_args.parse_args()
        print(args["id"])

        # Adding the passed information to the list of keywords
        keywords[keyword_id] = args
        print(keywords)
        return keywords[keyword_id], 201

# ------------------------------------------------------------------------


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

    # Generate the keywords and save to the downloads file
    generateKeywords_from_file('uploads/{}'.format(f.filename))

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


api.add_resource(Keyword, "/keyword/<int:keyword_id>")

if __name__ == '__main__':
    app.run(debug=True)

