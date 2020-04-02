from flask import Flask
import json
import requests
import random


app = Flask(__name__)

@app.route('/', methods=['GET' , 'POST'])
def rand_int():
  
  url = 'https://randomuser.me/api/?gender=female'
  r = requests.get(url)
  js = r.json()
  gender = str(js["results"][0]["gender"])
  first = str(js["results"][0]["name"]["first"])
  last = str(js["results"][0]["name"]["last"])
  age = str(js["results"][0]["dob"]["age"])  
  return gender + first + last + age

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5001, debug=True)
