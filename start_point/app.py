from flask import Flask
import json
import requests
import random


app = Flask(__name__)

@app.route('/', methods=['GET' , 'POST'])
def start_point():
  
  url = 'https://randomuser.me/api/?nat=us'
  r = requests.get(url)
  js = r.json()
  start_point = str(js["results"][0]["location"]["city"])
  
  return start_point

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5002, debug=True)
