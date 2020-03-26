from flask import Flask, Request, Response
import requests
import random
from os import getenv


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def core_service():

  rand_str = requests.get('http://40.69.63.132:5003/')
  final_res = str(rand_str.text)

  return "the final random number and string put together are " + str(final_res) #,  {"rand_int":rand_int} ,"asdasdasdasdad"
if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)

