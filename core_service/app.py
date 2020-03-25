from flask import Flask, Request, Response
import requests
import random
from os import getenv


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def core_service():
     
  final_result = requests.get('http://40.69.63.132:5007/')

  return str(final_result) #,  {"rand_int":rand_int} ,"asdasdasdasdad"
if __name__=='__main__':
  app.run(host='0.0.0.0', port=5007, debug=True)

