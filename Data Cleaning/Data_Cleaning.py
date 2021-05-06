#NBA PLAYER CLUSTERING PROJ FROM 2020-2021 BASKETBALL SEASON 
#Exploritory Data Analysis
#-Samruth

import pandas as pd
import seaborn as sb
import matplotlib.pyplot as mplt 


#import data

players = pd.read_csv('Full_NBA_Player_Stats.csv')
players2 = pd.read_csv('NBAplayersDATA.csv')

players2['OREB%'] = players2['OREB%'].apply(lambda x: x.split('%')[0])
players2['DREB%'] = players2['DREB%'].apply(lambda x: x.split('%')[0])
players2['USG%'] = players2['USG%'].apply(lambda x: x.split('%')[0])
players2['TS%'] = players2['TS%'].apply(lambda x: x.split('%')[0])
players2['AST%'] = players2['AST%'].apply(lambda x: x.split('%')[0])
players2['DREB%'] = pd.to_numeric(players2['DREB%'])
players2['OREB%'] = pd.to_numeric(players2['OREB%'])
players2['USG%'] = pd.to_numeric(players2['USG%'])
players2['TS%'] = pd.to_numeric(players2['TS%'])
players2['AST%'] = pd.to_numeric(players2['AST%'])

#df_unique['number_of_apps'] = minus_BATFandO.astype(str).astype(int)
players2 = players2.apply(lambda x: x.replace('%', ''))

#fixing height format in pandas

players2['first'] = players2['HEIGHT'].apply(lambda x: x.split('-')[0])
players2['second'] = players2['HEIGHT'].apply(lambda x: x.split('-')[1])
players2['5_feet'] = players2['second'].apply(lambda x: 5 if 'May' in x else 0)
players2['6_feet'] = players2['second'].apply(lambda x: 6 if 'Jun' in x else 0)
players2['7_feet'] = players2['second'].apply(lambda x: 7 if 'Jul' in x else 0)
players2['6_feet2'] = players2['first'].apply(lambda x: 6 if 'Jun' in x else 0)
players2['7_feet2'] = players2['first'].apply(lambda x: 7 if 'Jul' in x else 0)


NI = players2['first']
NI2 = NI.apply(lambda x: x.replace('Jun', '0').replace('Jul','0'))
players2['newinch'] = NI2.astype(str).astype(int)
players2['5_feet'] = pd.to_numeric(players2['5_feet'])
players2['6_feet'] = pd.to_numeric(players2['6_feet'])
players2['7_feet'] = pd.to_numeric(players2['7_feet'])
players2['6_feet2'] = pd.to_numeric(players2['6_feet2'])
players2['7_feet2'] = pd.to_numeric(players2['7_feet2'])

players2['comb_feet'] = players2['5_feet']+players2['6_feet']+players2['7_feet']+players2['6_feet2']+players2['7_feet2']
players2['inchesHeight'] = players2['comb_feet']*12+players2['newinch']

players2=players2.drop(columns=['HEIGHT', 'first', 'second', '5_feet', '6_feet', '7_feet', '6_feet2',\
                                      '7_feet2', 'comb_feet', 'newinch'] )
players2['HEIGHT']=players2['inchesHeight']
players2=players2.drop(columns=['inchesHeight'] )

#cleaning and adding Player3
players3 = pd.read_csv('sal_pos_player.csv')
sal = players3['SALARY']
sal = sal.apply(lambda x: x.replace('--', '0'))



players3['SALARY'] = sal.astype(str).astype(int)


#exporting csv files from pandas

#new player2 file 
players2.to_csv('Full_NBA_Player_Stats2.csv', index = False)

players = pd.read_csv('Full_NBA_Player_Stats.csv')
players_2 = pd.read_csv('Full_NBA_Player_Stats2.csv')
totalstats = pd.merge(players, players_2, on="Player")
totalstats = pd.merge(totalstats, players3, on="Player")


#combineing both data sets
totalstats.to_csv('total_Stats.csv', index = False)








