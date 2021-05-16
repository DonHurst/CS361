import requests

BASE = "http://127.0.0.1:5000/"
# BASE = "http://flip3.engr.oregonstate.edu:8993/"

data = {"title": "A TEST", "keyword_list": ["Hello", "Goodbye", "great success"]}
# 		{"title": "Hello2", "jsonString": "Goodbye2"},
# 		{"title": "Hello3", "jsonString": "Goodbye3"}]

# for i in range(len(data)):
# # 	data[i]["id"] = i
response = requests.put(BASE + "keyword" , data)

# response = requests.put(BASE + "keyword/1" + str[i], data[i])
# print(response)



response=requests.get(BASE + "keyword")
print(response.json())
# response=requests.get(BASE + "keyword/1")
# print(response.json())
# response=requests.get(BASE + "keyword/2")
# print(response.json())