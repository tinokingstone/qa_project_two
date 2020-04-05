from flask import Flask
from application import app
import requests
import random


@app.route('/', methods=['GET' , 'POST'])
def rand_int():
  rand_int = ""
  for i in range(16):
      rand_int += str(random.randint(0, 9))

  #return str(random.randint(0, 9))
  return rand_int #, {"rand_int":rand_int} ,"asdasdasdasdad"

