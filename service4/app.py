from flask import Flask, Request, Response
import requests
import random
from os import getenv


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def service4():
     
  rand_str = requests.get('http://localhost:5002/')
  rand_int = requests.get('http://localhost:5001/')  
  str_int = str(rand_str.text) + str(rand_int.text) 

  return str(str_int) #,  {"rand_int":rand_int} ,"asdasdasdasdad"
if __name__=='__main__':
  app.run(host='0.0.0.0', port=5003, debug=True)

