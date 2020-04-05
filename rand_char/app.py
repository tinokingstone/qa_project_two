from flask import Flask, jsonify
import json
import requests
import random


app = Flask(__name__)

@app.route('/', methods=['GET' , 'POST'])
def rand_int():

  url = 'https://randomuser.me/api/?gender=male'
  r = requests.get(url)
  js = r.json()
  gender = str(js["results"][0]["gender"])
  first = str(js["results"][0]["name"]["first"])
  last = str(js["results"][0]["name"]["last"])
  age = str(js["results"][0]["dob"]["age"])
  img = str(js["results"][0]["picture"]["thumbnail"])
  return jsonify ({'gender' : gender , 'first' : first , 'last' : last , 'age' : age , 'img' : img})  #gender + first + last + age + img

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5001, debug=True)

