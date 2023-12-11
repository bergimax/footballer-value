#!/usr/bin/env python
# coding: utf-8

import requests
import numpy as np

url = 'http://localhost:9696/predict'

#Player: 2075
#val expected: 80000000

player = {
  "team": "ac_milan", 
  "name": "rafael_leão", 
  "position": "attack-leftwinger", 
  "height": 180.0, 
  "age": 23.0, 
  "appearance": 90, 
  "goals": 0.403708, 
  "assists": 0.363337, 
  "yellow_cards": 0.134569, 
  "second_yellow_cards": 0.013457, 
  "red_cards": 0.0, 
  "goals_conceded": 0.0, 
  "clean_sheets": 0.0, 
  "minutes_played": 6688, 
  "days_injured": 237, 
  "games_injured": 34, 
  "award": 6, 
  "highest_value": 18.258162
}

requests.post(url, json=player)

requests.post(url, json=player).json()

response = requests.post(url, json=player).json()

rx = np.expm1(response['curr_value'])
print('The market value is: ', rx )
#value expected: 6000000