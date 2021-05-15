from flask import Flask, render_template, url_for, json, redirect, request, send_file, flash
from gensim.summarization import keywords
import os

# Variable for the root directory of the project 
basedir = os.path.abspath(os.path.dirname(__file__))

def generateKeywords_from_file(FILE_PATH):

    with open(FILE_PATH) as f:

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

def generateKeywords_from_api():
	pass
