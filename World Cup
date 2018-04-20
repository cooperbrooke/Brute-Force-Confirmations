# This World Cup 2018 Pool generator uses the power rankings of the 32 qualifying teams as an indicator of strength.
# To ensure fairness in distribution of teams, each participant is guaranteed to receive one team from each "grouping"
# where a "grouping" is manually defined to a block of seeds corresponding to the number of players

import pandas as pd
from sklearn.utils import shuffle

# List all teams
teams = ["Brazil", "Germany", "France", "Spain", "Portugal", "Uruguay", "Argentina", "Belgium", "England", "Columbia", "Mexico", "Russia", "Croatia", "Poland", "Switzerland", "Costa Rica", "Denmark", "Iceland", "Peru", "Sweden", "South Korea", "Nigeria", "Japan", "Serbia", "Egypt", "Australia", "Senegal", "Panama", "Morocco", "Iran", "Tunisia", "Saudia Arabia"]

# Receive inputs for number of participants and number of teams/participant
people = int(input("How many people are playing: "))
picks = int(input("How many teams per person: "))

# Condense the number of teams to the amount necessary based on inputs
teams = teams[:(people*picks)]

# Input teams into a Dataframe
df = pd.DataFrame({'Team':teams})

# Shape the Dataframe into a matrix such that the top row has the top "picks" amount of teams and so and so forth
relist = df.values.reshape(picks,people)

# Transform the Dataframe back into a list of lists for manipulation
relist = relist.tolist()

# Create function to go through each list and shuffle the teams
x = 0
for i in relist:
    relist[x] = shuffle(i)
    x += 1

# Transform the shuffled data back into a Dataframe    
final_df = pd.DataFrame(relist)

# Create a function that takes inputs for players name and adds them to a list
player_names = []

for i in range(1,people+1):
    name = input("Please enter Player {0}'s name: ".format(i))
    player_names.append(name)

# Add the names to the dataframe
final_df.columns = player_names

# Print the final results
print(final_df)
    
    
