# -*- coding: utf-8 -*-
"""
Created on Tue May  4 16:25:51 2021

@author: samru
"""

import pandas as pd
import seaborn as sb
import matplotlib.pyplot as mplt 

players = pd.read_csv('Full_NBA_Player_Stats.csv')
players2 = pd.read_csv('Full_NBA_Player_Stats2.csv')

#Getting the size of ouw data sets(606 columns(Players) and 23 rows(Stats))

players.shape
players2.shape

#Finding the mean details

players.mean()
players2.mean()

#****Cool information, Put into TABLEAU later*****

#Finding The coorelation between stats

cmap = sb.diverging_palette(220, 42, as_cmap=True)
    #heatmap         
sb.heatmap(players[["GP", "MPG", "FGM", "FGA", "FG%", "3PM", "3PA", "3P%", "FTM", "FTA", "FT%", "TOV", "PF", "ORB",\
                    "DRB", "RPG", "APG", "SPG", "BPG", "PPG"]].corr(), vmax=1, center=0,cmap=cmap, square=True,linewidths=.5, cbar_kws={"shrink":.5})
sb.heatmap(players2[["AGE", "WEIGHT", "GP", "PTS", "REB", "AST", "NETRTG", "OREB%", "DREB%", "USG%", "TS%",\
                    "AST%"]].corr(), vmax=1, center=0,cmap=cmap, square=True,linewidths=.5, cbar_kws={"shrink":.5})
    #Correlation dataframe
corr_df=players[["GP", "MPG", "FGM", "FGA", "FG%", "3PM", "3PA", "3P%", "FTM", "FTA", "FT%", "TOV", "PF", "ORB",\
                    "DRB", "RPG", "APG", "SPG", "BPG", "PPG"]].corr()
corr_df2=players2[["AGE", "WEIGHT", "GP", "PTS", "REB", "AST", "NETRTG", "OREB%", "DREB%", "USG%", "TS%",\
                    "AST%"]].corr()
    #total pairplot
sb.pairplot(players[["GP", "MPG", "FGM", "FGA", "FG%", "3PM", "3PA", "3P%", "FTM", "FTA", "FT%",\
                      "TOV", "PF", "ORB", "DRB", "RPG", "APG", "SPG", "BPG", "PPG"]])
sb.pairplot(players2[["AGE", "WEIGHT", "GP", "PTS", "REB", "AST", "NETRTG", "OREB%", "DREB%", "USG%", "TS%",\
                    "AST%"]])
    
    
    #slight negative corralation    
sb.pairplot(players[["3P%", "ORB"]])
    #no corralation    
sb.pairplot(players[["FT%", "BPG"]])
    #strong positive corralation    
sb.pairplot(players[["TOV", "APG"]])
