# simulate a given English Premier League match using expected goals for (xG)
# and expeced goals against (xGA) for 2018/19 season
# v1.0 - 15 August 2019

import numpy as np

# values are average xG and xGA for 2018/19 season
# source: https://understat.com/league/EPL/2018
team_goals = {
    "ARS": [1.71, 1.51],    "BOU": [1.55, 1.64],    "BHA": [0.97, 1.64],    "BUR": [1.18, 1.74],
    "CAR": [1.10, 1.75],    "CHE": [1.68, 1.00],    "CRY": [1.33, 1.39],    "EVE": [1.42, 1.30],
    "FUL": [1.12, 1.94],    "HUD": [0.76, 1.77],    "LEI": [1.37, 1.17],    "LIV": [2.09, 0.77],
    "MCI": [2.47, 0.68],    "MUN": [1.81, 1.38],    "NEW": [1.05, 1.51],    "SOT": [1.31, 1.56],
    "SPU": [1.63, 1.29],    "WAT": [1.36, 1.67],    "WHU": [1.26, 1.73],    "WOL": [1.40, 1.13]
}

# league-wide variables from 2018/19 season
avg_goals_for = 1.40
home_adv = 1.09
away_adv = 0.91
home_team = ""

# generate random match score until user quits
print("\n(Enter 'Q' as home team to quit)")
while(home_team != "Q"):
    home_team = input("\nHome team: ")
    if(home_team != "Q"):
        away_team = input("Away team: ")

        home_xG = round((team_goals[home_team][0] * team_goals[away_team][1]
            * home_adv) / avg_goals_for, 3)
        away_xG = round((team_goals[away_team][0] * team_goals[home_team][1]
            * away_adv) / avg_goals_for, 3)

        home_goals = np.random.poisson(home_xG, 1)
        away_goals = np.random.poisson(away_xG, 1)

        print("\n%s %d-%d %s" % (home_team, home_goals, away_goals, away_team))
