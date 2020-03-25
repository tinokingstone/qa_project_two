from flask import Flask
import requests
import random


app = Flask(__name__)

@app.route('/', methods=['GET' , 'POST'])
def rand_int():
  rand_int = ""
  for i in range(4):
      rand_int += str(random.randint(0, 9))
  
  #return str(random.randint(0, 9))
  return rand_int #, {"rand_int":rand_int} ,"asdasdasdasdad"
if __name__=='__main__':
  app.run(host='0.0.0.0', port=5001, debug=True)

