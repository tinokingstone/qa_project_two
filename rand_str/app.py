from flask import Flask
import requests
import random


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def rand_str():
  #rand_int = ""
  #for i in range(4):
  #    rand_int += str(random.randint(0, 9))

  rand_str = ""
  letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  for i in range(8):
      rand_str += str(random.choice(letters))    


  #return str(random.randint(0, 9))
  return rand_str, {"rand_str":rand_str} #"asdasdasdasdad"
if __name__=='__main__':
  app.run(host='0.0.0.0', port=5002, debug=True)

