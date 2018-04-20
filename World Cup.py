import pandas as pd
import numpy as np

from sklearn.utils import shuffle


teams = ["Brazil", "Germany", "France", "Spain", "Portugal", "Uruguay", "Argentina", "Belgium", "England", "Columbia", "Mexico", "Russia", "Croatia", "Poland", "Switzerland", "Costa Rica", "Denmark", "Iceland", "Peru", "Sweden", "South Korea", "Nigeria", "Japan", "Serbia", "Egypt", "Australia", "Senegal", "Panama", "Morocco", "Iran", "Tunisia", "Saudia Arabia"]

people = int(input("How many people are playing: "))
picks = int(input("How many teams per person: "))

teams = teams[:(people*picks)]



df = pd.DataFrame({'Team':teams})

relist = df.values.reshape(picks,people)

relist = relist.tolist()

x = 0

for i in relist:
    relist[x] = shuffle(i)
    x += 1

final_df = pd.DataFrame(relist)

player_names = []

for i in range(1,people+1):
    name = input("Please enter Player {0}'s name: ".format(i))
    player_names.append(name)
    
final_df.columns = player_names

print(final_df)
    
    
