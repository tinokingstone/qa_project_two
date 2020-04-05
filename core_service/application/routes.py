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
  #env_ip = str(getenv('ENV_IP'))
  #url = "http://"+str(env_ip)+":5002/"


  start_point = requests.get('http://51.140.240.158:5002/')
  end_point = requests.get('http://51.140.240.158:5003/')
  survive_weapon = requests.get('http://51.140.240.158:5006/')
  survive_character = requests.get('http://51.140.240.158:5001/')

  url = "http://51.140.240.158:5001/"
  r = requests.get(url)
  js = r.json()
  first = str(js["first"])
  last = str(js["last"])
  age = str(js["age"])
  gender = str(js["gender"])
  img = str(js["img"])


  url2 = 'http://51.140.240.158:5005/'

  r = requests.get(url2)
  js = r.json()
  agility = str(js["Agility"])
  charisma = str(js["Charisma"])
  endurance = str(js["Endurance"])
  intelligence = str(js["Intelligence"])
  strength = str(js["Strength"])


  start_point = str(start_point.text)
  end_point = str(end_point.text)

  survive_character = str(survive_character.text)


  survive_weapon = str(survive_weapon.text)
  rand_obj_fin = str(survive_weapon)
  form = Rand_obj_f()

  all_saves = rand_obj.query.all()

  if form.validate_on_submit():
      rand_obj_insert = rand_obj(first=first, last=first, age=age ,gender=gender , img=img ,agility=agility,charisma=charisma,endurance=endurance,intelligence=intelligence,strength=strength,weapon=survive_weapon,end_point=end_point,start_point=start_point,rand_item="0")
      db.session.add(rand_obj_insert)
      db.session.commit()
      flash('item added to the database')
      return redirect(url_for('landing'))
  return render_template('landing.html', title='landing', form=form , end_point=end_point, start_point=start_point, survive_character=survive_character, survive_weapon=survive_weapon,  all_saves=all_saves, env_ip=url , first=first, last=last, gender=gender, age=age, img=img ,agility=agility,charisma=charisma,endurance=endurance,intelligence=intelligence,strength=strength )
