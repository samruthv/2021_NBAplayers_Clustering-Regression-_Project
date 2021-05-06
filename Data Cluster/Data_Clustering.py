#NBA PLAYER CLUSTERING PROJ FROM 2020-2021 BASKETBALL SEASON 
#Clustering Players
#-Samruth

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as mplt 
import seaborn as sb

#import data

players = pd.read_csv('Full_NBA_Player_Stats.csv')
players_2 = pd.read_csv('Full_NBA_Player_Stats2.csv')
totalstats = pd.read_csv('total_Stats.csv')

#Cleaning data

    #removing rows that hinder the model
cleanedDF=totalstats.drop(columns=['#'] )

    #dividing cetrain stats my minutes played to not let the minutes played infuence the model
cleanedDF['FGM/Min']=cleanedDF.FGM/cleanedDF.MPG
cleanedDF['FGA/Min']=cleanedDF.FGA/cleanedDF.MPG
cleanedDF['3PM/Min']=cleanedDF['3PM']/cleanedDF.MPG
cleanedDF['3PA/Min']=cleanedDF['3PA']/cleanedDF.MPG
cleanedDF['FTM/Min']=cleanedDF.FTM/cleanedDF.MPG
cleanedDF['FTA/Min']=cleanedDF.FTA/cleanedDF.MPG
cleanedDF['TOV/Min']=cleanedDF.TOV/cleanedDF.MPG
cleanedDF['PF/Min']=cleanedDF.PF/cleanedDF.MPG
cleanedDF['ORB/Min']=cleanedDF.ORB/cleanedDF.MPG
cleanedDF['DRB/Min']=cleanedDF.DRB/cleanedDF.MPG
cleanedDF['APG/Min']=cleanedDF.APG/cleanedDF.MPG
cleanedDF['FTA/Min']=cleanedDF.FTA/cleanedDF.MPG
cleanedDF['SPG/Min']=cleanedDF.SPG/cleanedDF.MPG
cleanedDF['BPG/Min']=cleanedDF.BPG/cleanedDF.MPG
cleanedDF['PPG/Min']=cleanedDF.PPG/cleanedDF.MPG

    #removing stats that we changed above to /MIN
cleanedDF=cleanedDF.drop(columns=['GP_x', 'FGM','FGA','3PM','3PA','FTM','FTA','TOV','PF','ORB',\
                                  'DRB','APG','FTA','SPG','BPG', 'PPG', 'MPG', 'Team', 'TEAM', 'AGE', 'HEIGHT', 'WEIGHT', 'COLLEGE',\
                                      'COUNTRY', 'DRAFT ROUND', 'DRAFT NUMBER', 'GP_y', 'PTS', 'REB', 'AST', 'NETRTG', 'RPG', 'DRAFT YEAR','USG%' ] )

#clustering using KMeans
    #Creating model with 10 clusters
model = KMeans(n_clusters=10, random_state=10)
    #Getting numeric data and removing columns with missing data
good_columns = cleanedDF._get_numeric_data().dropna(axis=1)
    #Training model
print(good_columns)
model.fit(good_columns)

labels = model.labels_
print(labels)
totalstats['labeledGroup']=labels 

#Plot Players by cluster

from sklearn.decomposition import PCA
pca_2 = PCA(2)
plot_columns = pca_2.fit_transform(good_columns)
plot_columns
mplt.scatter(x=plot_columns[:,0], y=plot_columns[:,1], c=labels)
mplt.show

name_cluster=[]

for index, row in cleanedDF.iterrows():
    playername=cleanedDF.Player[index]
    name = good_columns.loc[totalstats['Player']==playername,:]
    name_list = name.values.tolist()
    storedval=model.predict(name_list)
    name_cluster.append(storedval)

totalstats['predictedGroup']=name_cluster 

LeBron = good_columns.loc[totalstats['Player']=='LeBron James',:]
Curry = good_columns.loc[totalstats['Player']=='Stephen Curry',:]
Jokic = good_columns.loc[totalstats['Player']=='Nikola Jokic',:]
Durant = good_columns.loc[totalstats['Player']=='Kevin Durant',:]
will = good_columns.loc[totalstats['Player']=='Lou Williams',:]

LeBron_list = LeBron.values.tolist()
Curry_list = Curry.values.tolist()
Jokic_list = Jokic.values.tolist()
Durant_list = Durant.values.tolist()
will_list = will.values.tolist()

#Predicting models
LeBron_Cluster=model.predict(LeBron_list)
Curry_Cluster=model.predict(Curry_list)
Jokic_Cluster=model.predict(Jokic_list)
Durant_Cluster=model.predict(Durant_list)
will_Cluster=model.predict(will_list)
print(LeBron_Cluster)
print(Curry_Cluster)
print(Jokic_Cluster)
print(Durant_Cluster)
print(will_Cluster)

stats=totalstats[["#", "labeledGroup"]].corr()
sb.pairplot(totalstats[["#", "labeledGroup"]])

#we tried looking if how good the player was is correlated to salary
#we get the correlation to be 0.0687. So it safe to say no coorelation
sal_corr=totalstats[["SALARY", "labeledGroup"]].corr()


#But lets look at individual stats to salary

#Salary and PPG are 72.7% correlated
sal_corr=totalstats[["SALARY", "PPG"]].corr()
#Salary and AST are 67.9% correlated
sal_corr=totalstats[["SALARY", "AST"]].corr()
#Salary and RPG are 48.9% correlated
sal_corr=totalstats[["SALARY", "RPG"]].corr()



#%%

#In this cell we try to cluster players into 2 catagories: good and bad players
#we will bchoosing which varibales to use to see how the model changes 

#import data

players = pd.read_csv('Full_NBA_Player_Stats.csv')
players_2 = pd.read_csv('Full_NBA_Player_Stats2.csv')
totalstats = pd.merge(players, players_2, on="Player")

#Cleaning data

    #removing rows that hinder the model
cleanedDF=totalstats.drop(columns=['#'] )

    #removing stats that we changed above to /MIN
cleanedDF=cleanedDF.drop(columns=['GP_x', 'Team', 'TEAM', 'AGE', 'HEIGHT', 'WEIGHT', 'COLLEGE',\
                                      'COUNTRY', 'DRAFT ROUND', 'DRAFT NUMBER', 'GP_y', 'DRAFT YEAR' ] )

#clustering using KMeans
    #Creating model with 10 clusters
model = KMeans(n_clusters=2, random_state=10)
    #Getting numeric data and removing columns with missing data
good_columns = cleanedDF._get_numeric_data().dropna(axis=1)
    #Training model
print(good_columns)
model.fit(good_columns)

labels = model.labels_
print(labels)
totalstats['labeledGroup']=labels 

#Plot Players by cluster

from sklearn.decomposition import PCA
pca_2 = PCA(2)
plot_columns = pca_2.fit_transform(good_columns)
plot_columns
mplt.scatter(x=plot_columns[:,0], y=plot_columns[:,1], c=labels)
mplt.show

name_cluster=[]

for index, row in cleanedDF.iterrows():
    playername=cleanedDF.Player[index]
    name = good_columns.loc[totalstats['Player']==playername,:]
    name_list = name.values.tolist()
    storedval=model.predict(name_list)
    name_cluster.append(storedval)

totalstats['predictedGroup']=name_cluster 

LeBron = good_columns.loc[totalstats['Player']=='LeBron James',:]
Curry = good_columns.loc[totalstats['Player']=='Stephen Curry',:]
Jokic = good_columns.loc[totalstats['Player']=='Nikola Jokic',:]
Durant = good_columns.loc[totalstats['Player']=='Kevin Durant',:]
will = good_columns.loc[totalstats['Player']=='Lou Williams',:]

LeBron_list = LeBron.values.tolist()
Curry_list = Curry.values.tolist()
Jokic_list = Jokic.values.tolist()
Durant_list = Durant.values.tolist()
will_list = will.values.tolist()

#Predicting models
LeBron_Cluster=model.predict(LeBron_list)
Curry_Cluster=model.predict(Curry_list)
Jokic_Cluster=model.predict(Jokic_list)
Durant_Cluster=model.predict(Durant_list)
will_Cluster=model.predict(will_list)
print(LeBron_Cluster)
print(Curry_Cluster)
print(Jokic_Cluster)
print(Durant_Cluster)
print(will_Cluster)


#switching 1's to 0's and 0's to 1's
for index, row in cleanedDF.iterrows():
    if totalstats.labeledGroup[index] == 0:
        totalstats.labeledGroup[index] = 1
    else:
        totalstats.labeledGroup[index] = 0

    
cleanedDF['labels']=labels

#ranking what percent of each team consits of good players
pd.pivot_table(totalstats, index = 'Team', values = 'labeledGroup').sort_values('labeledGroup',ascending=False)


#look at the correlation between the models take on if they are a good or bad player and their rank on their team.
#there is a negative coorelation(-0.7867010511245318) between a good(1) and bad player(1) and rank on team(lower rank is better)
#So our model is good
stats=totalstats[["#", "labeledGroup"]].corr()
sb.pairplot(totalstats[["#", "labeledGroup"]])

#we tried looking if how good the player was is correlated to height
#we get the correlation to be -0.019. So it safe to say no coorelation
height_model_corr=totalstats[["HEIGHT", "labeledGroup"]].corr()

#there is a negative correlation(-0.7867010511245318) between a good(1) and bad player(1) and rank on team(lower rank is better)
#So our model is good



#%%
#Here we try cluster NBA players with 'PPG', 'AST' and 'RPG'
#The cluster we get is shows is not very useful. We get the a player good in one of those catagories is typically good at the other ones aswell.
#The cluster is just splitting up players by how good they are

players = pd.read_csv('Full_NBA_Player_Stats.csv')
players_2 = pd.read_csv('Full_NBA_Player_Stats2.csv')
totalstats = pd.merge(players, players_2, on="Player")

#Cleaning data

    #removing rows that hinder the model
cleanedDF=totalstats.drop(columns=['#'] )

    #removing stats that we changed above to /MIN
cleanedDF=cleanedDF.drop(columns=['GP_x', 'FGM','FGA','3PM','3PA','FTM','FTA','PF','ORB', 'FT%', 'FG%','TOV',\
                                  'DRB','APG','FTA','SPG','BPG', '3P%', 'MPG', 'Team', 'TEAM', 'AGE', 'HEIGHT', 'WEIGHT', 'COLLEGE',\
                                      'COUNTRY', 'DRAFT ROUND', 'DRAFT NUMBER', 'GP_y', 'PTS', 'REB', 'AST%', 'NETRTG', 'OREB%', 'DRAFT YEAR','USG%', 'TS%', 'DREB%' ] )

#clustering using KMeans
    #Creating model with 10 clusters
model = KMeans(n_clusters=4, random_state=10)
    #Getting numeric data and removing columns with missing data
good_columns = cleanedDF._get_numeric_data().dropna(axis=1)
    #Training model
print(good_columns)
model.fit(good_columns)

labels = model.labels_
print(labels)
totalstats['labeledGroup']=labels 

#Plot Players by cluster

from sklearn.decomposition import PCA
pca_2 = PCA(2)
plot_columns = pca_2.fit_transform(good_columns)
plot_columns
mplt.scatter(x=plot_columns[:,0], y=plot_columns[:,1], c=labels)
mplt.show

name_cluster=[]

for index, row in cleanedDF.iterrows():
    playername=cleanedDF.Player[index]
    name = good_columns.loc[totalstats['Player']==playername,:]
    name_list = name.values.tolist()
    storedval=model.predict(name_list)
    name_cluster.append(storedval)

totalstats['predictedGroup']=name_cluster 

#test case models
'''
LeBron = good_columns.loc[totalstats['Player']=='LeBron James',:]
Curry = good_columns.loc[totalstats['Player']=='Stephen Curry',:]
Jokic = good_columns.loc[totalstats['Player']=='Nikola Jokic',:]
Durant = good_columns.loc[totalstats['Player']=='Kevin Durant',:]
will = good_columns.loc[totalstats['Player']=='Lou Williams',:]

LeBron_list = LeBron.values.tolist()
Curry_list = Curry.values.tolist()
Jokic_list = Jokic.values.tolist()
Durant_list = Durant.values.tolist()
will_list = will.values.tolist()

#Predicting models
LeBron_Cluster=model.predict(LeBron_list)
Curry_Cluster=model.predict(Curry_list)
Jokic_Cluster=model.predict(Jokic_list)
Durant_Cluster=model.predict(Durant_list)
will_Cluster=model.predict(will_list)
print(LeBron_Cluster)
print(Curry_Cluster)
print(Jokic_Cluster)
print(Durant_Cluster)
print(will_Cluster)
cleanedDF['labels']=labels
'''

#%%






#Cleaning data

    #removing rows that hinder the model
cleanedDF=players.drop(columns=['#'] )

    #dividing cetrain stats my minutes played to not let the minutes played infuence the model
cleanedDF['FGM/Min']=cleanedDF.FGM/cleanedDF.MPG
cleanedDF['FGA/Min']=cleanedDF.FGA/cleanedDF.MPG
cleanedDF['3PM/Min']=cleanedDF['3PM']/cleanedDF.MPG
cleanedDF['3PA/Min']=cleanedDF['3PA']/cleanedDF.MPG
cleanedDF['FTM/Min']=cleanedDF.FTM/cleanedDF.MPG
cleanedDF['FTA/Min']=cleanedDF.FTA/cleanedDF.MPG
cleanedDF['TOV/Min']=cleanedDF.TOV/cleanedDF.MPG
cleanedDF['PF/Min']=cleanedDF.PF/cleanedDF.MPG
cleanedDF['ORB/Min']=cleanedDF.ORB/cleanedDF.MPG
cleanedDF['DRB/Min']=cleanedDF.DRB/cleanedDF.MPG
cleanedDF['APG/Min']=cleanedDF.APG/cleanedDF.MPG
cleanedDF['FTA/Min']=cleanedDF.FTA/cleanedDF.MPG
cleanedDF['SPG/Min']=cleanedDF.SPG/cleanedDF.MPG
cleanedDF['BPG/Min']=cleanedDF.BPG/cleanedDF.MPG
cleanedDF['PPG/Min']=cleanedDF.PPG/cleanedDF.MPG

    #removing stats that we changed above to /MIN
cleanedDF=cleanedDF.drop(columns=['GP', 'FGM','FGA','3PM','3PA','FTM','FTA','TOV','PF','ORB','DRB','APG','FTA','SPG','BPG', 'PPG', 'MPG' ] )


#clustering using KMeans
    #Creating model with 10 clusters
model = KMeans(n_clusters=10, random_state=5)
    #Getting numeric data and removing columns with missing data
good_columns = cleanedDF._get_numeric_data().dropna(axis=1)
    #Training model
model.fit(good_columns)

labels = model.labels_
print(labels)
players['labeledGroup']=labels 

#Plot Players by cluster

from sklearn.decomposition import PCA
pca_2 = PCA(2)
plot_columns = pca_2.fit_transform(good_columns)
plot_columns
mplt.scatter(x=plot_columns[:,0], y=plot_columns[:,1], c=labels)
mplt.show

name_cluster=[]

for index, row in cleanedDF.iterrows():
    playername=cleanedDF.Player[index]
    name = good_columns.loc[players['Player']==playername,:]
    name_list = name.values.tolist()
    storedval=model.predict(name_list)
    name_cluster.append(storedval)

players['predictedGroup']=name_cluster 





LeBron = good_columns.loc[players['Player']=='LeBron James',:]
Curry = good_columns.loc[players['Player']=='Stephen Curry',:]
Jokic = good_columns.loc[players['Player']=='Nikola Jokic',:]
Durant = good_columns.loc[players['Player']=='Kevin Durant',:]
will = good_columns.loc[players['Player']=='Lou Williams',:]

LeBron_list = LeBron.values.tolist()
Curry_list = Curry.values.tolist()
Jokic_list = Jokic.values.tolist()
Durant_list = Durant.values.tolist()
will_list = will.values.tolist()

#Predicting models
LeBron_Cluster=model.predict(LeBron_list)
Curry_Cluster=model.predict(Curry_list)
Jokic_Cluster=model.predict(Jokic_list)
Durant_Cluster=model.predict(Durant_list)
will_Cluster=model.predict(will_list)
print(LeBron_Cluster)
print(Curry_Cluster)
print(Jokic_Cluster)
print(Durant_Cluster)
print(will_Cluster)



