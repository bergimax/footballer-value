#!/usr/bin/env python
# coding: utf-8

import requests
import numpy as np

url = 'http://localhost:9696/predict'

#Player: 149

player = {
  "team": "southampton_fc", 
  "name": "stuart_armstrong", 
  "position": "midfield-centralmidfield", 
  "height": 183.0, 
  "age": 31.0, 
  "appearance": 65, 
  "goals": 0.133294, 
  "assists": 0.053318, 
  "yellow_cards": 0.186611, 
  "second_yellow_cards": 0.0, 
  "red_cards": 0.0, 
  "goals_conceded": 0.0, 
  "clean_sheets": 0.0, 
  "minutes_played": 3376, 
  "days_injured": 259, 
  "games_injured": 39, 
  "award": 8, 
  "current_value": 15.60727,
  "highest_value": 15.894952
}

requests.post(url, json=player)

requests.post(url, json=player).json()

response = requests.post(url, json=player).json()

rx = np.expm1(response['curr_value'])
print('The market value is: ', rx )
#value expected: 6000000