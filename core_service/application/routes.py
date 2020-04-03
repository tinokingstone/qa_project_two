import os
from os import getenv
import secrets
from flask import render_template, url_for, flash, redirect, request
from application import app , db 
from application.forms import Rand_obj_f
from application.models import rand_obj
from sqlalchemy import MetaData, Column
import requests
import random

@app.route('/', methods=['GET' , 'POST' ])
@app.route('/landing', methods=['GET' , 'POST' ])
def landing():
  env_ip = str(getenv('ENV_IP'))
  url = "http://"+str(env_ip)+":5002/"
  start_point = requests.get('http://40.69.63.132:5002/')
  end_point = requests.get('http://40.69.63.132:5003/')
  survive_character = requests.get('http://40.69.63.132:5004/')
  final_res = str(start_point.text)
  final_res2 = str(end_point.text)
  survive_character = str(survive_character.text)

  rand_obj_fin = str("hello")
  form = Rand_obj_f()

  all_saves = rand_obj.query.all()

  if form.validate_on_submit():
      rand_obj_insert = rand_obj(rand_item=rand_obj_fin)
      db.session.add(rand_obj_insert)
      db.session.commit()
      flash('item added to the database')
      return redirect(url_for('landing'))
  return render_template('landing.html', title='landing', form=form , end_point=final_res, start_point=final_res2, survive_character=survive_character, all_saves=all_saves, env_ip=url )

