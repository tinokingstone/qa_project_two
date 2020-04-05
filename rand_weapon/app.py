from flask import Flask, jsonify
import json
import requests
import random


app = Flask(__name__)

@app.route('/', methods=['GET' , 'POST'])
def rand_weapon():

  url = 'http://51.140.240.158:5001/'
  url2 = 'http://51.140.240.158:5005/'

  r = requests.get(url)
  js = r.json()
  first = str(js["first"])
  last = str(js["last"])

  r = requests.get(url2)
  js = r.json()

  Agility = str(js["Agility"])
  Charisma = str(js["Charisma"])
  Endurance = str(js["Endurance"])
  Intelligence = str(js["Intelligence"])
  Strength = str(js["Strength"])

  allstats = Agility + Charisma + Endurance + Intelligence + Strength


  rand_loc = str(first)+str(last)
  rand_int = str(allstats)

  vowels = ["a", "e","i", "o", "u"]
  vowels_count = ""
  for v in vowels:
      for r in rand_loc:
          if v == r:
              vowels_count += r

  even_nums = ["2", "4", "6", "8", "0"]
  even_nums_count = ""
  for n in even_nums:
      for ri in rand_int:
          if n == ri:
              even_nums_count += r

  fin_val = len(vowels_count) + len(even_nums_count)

  weapons = [["rubber duck", "fork" , "butter knife" ,"baseball bat", "cross bow" ] ,[ "axe" , "samuri sword", "pistol" , "automatic rifle" , "sniper rifle" ] , ["grenade launcher"] ,["tank"]]
  tiers = ["0", "1", "2", "3"]

  if fin_val <= 23:
      tier = 0
      tier_option = weapons[tier]
      rand_wep = random.randrange((len(tier_option)) - 1)
      weapon_option = tier_option[rand_wep]
      return(weapon_option)

  elif fin_val <= 25:
      tier = 1
      tier_option = weapons[tier]
      rand_wep = random.randrange((len(tier_option)) - 1)
      weapon_option = tier_option[rand_wep]
      return(weapon_option)

  elif fin_val <= 27:
      tier = 2
      tier_option = weapons[tier]
      rand_wep = random.randrange((len(tier_option)))
      weapon_option = tier_option[rand_wep]
      return(weapon_option)

  elif fin_val >= 29:
      tier = 3
      tier_option = weapons[tier]
      rand_wep = random.randrange((len(tier_option)))
      weapon_option = tier_option[rand_wep]
      return(weapon_option)

  else:
      return("fail")

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5006, debug=True)
