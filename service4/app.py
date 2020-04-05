from flask import Flask, Request, Response
import requests
import random
from os import getenv

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def service4():
     
  #rand_str = requests.get('http://51.140.240.158:5002/')
  survive_character = requests.get('http://40.69.63.132:5001/')  
  start_point = requests.get('http://40.69.63.132:5002/')
  end_point = requests.get('http://40.69.63.132:5003/')
                                                                      
  survive_character = str(survive_character.text) 
  start_point = str(start_point.text)
  end_point = str(end_point.text)

  return str(survive_character) + str(start_point) + str(end_point)
if __name__=='__main__':
  app.run(host='0.0.0.0', port=5004, debug=True)

