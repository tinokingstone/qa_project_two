from flask import Flask, Request, Response
import requests
import random
from os import getenv


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def core_service():
  


    
  rand_str = requests.get('http://rand_str:5002')
  rand_int = requests.get('http://rand_int:5001')  
  str_int = str(rand_str) + str(rand_int) 
  #letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  #for i in range(16):
  #rand_str += str(random.choice(letters))    
  #return str(random.randint(0, 9))

  return rand_str
if __name__=='__main__':
  app.run(host='0.0.0.0', port=5002, debug=True)

