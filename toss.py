import sys
import json
import numpy
import os

script_dir = os.path.dirname(__file__) 

# Initiate Toss
# @params {Void}
# @returns {String}
def take_decision(weather, day_night):
    toss_data = json.load(open(script_dir + "/files/toss.json"))
    toss_won_team = numpy.random.choice(['Lengaburu','Enchai'], p=[0.5, 0.5]).lower()
    option = ""

    if toss_data[toss_won_team][weather] == toss_data[toss_won_team][day_night]:
        option = toss_data[toss_won_team][weather]
    else:
        option = numpy.random.choice([
            toss_data[toss_won_team][weather],
            toss_data[toss_won_team][day_night]
        ], p=[0.5, 0.5])    
    return toss_won_team, option
 