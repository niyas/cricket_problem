import sys
from toss import take_decision

# Get the command line arguments for Weather and Day/Night
weather = sys.argv[1]
day_night = sys.argv[2]

# Invoke method to take decision
team, decision = take_decision(weather, day_night)

print(team + " wins toss and " + decision)
