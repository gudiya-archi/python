import pandas as pd
import numpy as np

ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRj9eesx6RBBnFY1UiP0L2c7skH4n0Kw5_hbnVmwdPi7t7Je2T6aZBoRgMvbplWP4GmP4Bsa50yBQ2J/pub?output=csv"
matches = pd.read_csv(ipl_matches)

print(matches.head())

def teamsAPI():
    teams =  list(set(list(matches['Team1']) + list(matches['Team2'])))
    team_dict = {
        'teams': teams

    }
    return team_dict