import requests
from flask import Flask, render_template, url_for, json, redirect, request, send_file, flash
from gensim.summarization import keywords
import os
from keywordGenerator import generateKeywords_from_file, generateKeywords_from_api

# BASE = "https://www.don-hurst.com/keyword"
# BASE = "http://valchin.com/sendjson2021"
# BASE = "http://flip3.engr.oregonstate.edu:8993/"
BASE = "http://127.0.0.1:5000/keyword"

# data = {"title": "A TEST", "keyword_list": ["Hello", "Goodbye", "great success"]}
# 		{"title": "Hello2", "jsonString": "Goodbye2"},
# 		{"title": "Hello3", "jsonString": "Goodbye3"}]

# for i in range(len(data)):
# # 	data[i]["id"] = i
# response = requests.put(BASE + "keyword" , data)

# response = requests.put(BASE + "keyword/1" + str[i], data[i])
# print(response)

keyword_list = {}


response=requests.get(BASE)
# response=requests.get(BASE + "keyword")
print(response)
print(response.json())
print(type(response.json()))
# jsonString = response.json()
# print(jsonString)
# keywordsJson = generateKeywords_from_api(jsonString)





# print(keywordsJson)
# response=requests.get(BASE + "keyword/1")
# print(response.json())
# response=requests.get(BASE + "keyword/2")
# print(response.json())