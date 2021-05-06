import json

Developers = ["Housemarque", "Konami", "Bungie"]
gamedev = []

# Sample Json Data
jsonInfo = '{"Developer": "Konami", "Publisher": "Konami"} '

# This will read in the json file
with open('jsonFile.json') as f:
    data = json.load(f)

print(data)

# Converting the Python Dict to a string
jsonString = json.dumps(data, indent=2, sort_keys=True)

# print the string
print(jsonString)

# For all developers in our list
for dev in Developers:
    # if the developer is present in the string
    if dev in jsonString:
        #Append it to the dev
        gamedev.append(dev)

#printing the json file contents
print(gamedev)

# Parsing the Json Data
# obj = json.loads(jsonInfo)

# Printing Specific Data from JSON

