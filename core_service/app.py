from flask import Flask, render_template, url_for, flash, redirect, request
import requests
import random
from os import getenv


app = Flask(__name__)

@app.route('/', methods=['GET' , 'POST' ])
@app.route('/landing', methods=['GET' , 'POST' ])

def landing():
	
  return render_template('landing.html', title='landing')


  #return "the final random number and string put together are " + str(final_res) #,  {"rand_int":rand_int} ,"asdasdasdasdad"
if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)

