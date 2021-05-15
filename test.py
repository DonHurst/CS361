import requests

BASE = "http://127.0.0.1:5000/"

# data = [{"title": "Hello1", "jsonString": "Goodbye1"},
# 		{"title": "Hello2", "jsonString": "Goodbye2"},
# 		{"title": "Hello3", "jsonString": "Goodbye3"}]

# for i in range(len(data)):
# 	data[i]["id"] = i
# 	response = requests.put(BASE + "keyword/" + str(i), data[i])

# response = requests.put(BASE + "keyword/1" + str[i], data[i])
# print(response)

response=requests.get(BASE + "keyword/0")
print(response.json())
# response=requests.get(BASE + "keyword/1")
# print(response.json())
# response=requests.get(BASE + "keyword/2")
# print(response.json())