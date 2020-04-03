from flask import Flask
import json
import requests
import random


app = Flask(__name__)

@app.route('/', methods=['GET' , 'POST'])
def end_point():
  
  url = 'https://randomuser.me/api/?nat=gb'
  r = requests.get(url)
  js = r.json()
  end_point = str(js["results"][0]["location"]["city"])
  
  return end_point

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5003, debug=True)
