# 2021_NBAplayers_Clustering-Regression-_Project

  *As a huge sports and basketball fan, I wanted to work on a project the involed basketball players and statistics. My goal for this project was to really dive into what seperates ever player interms or play style. This was a challenging iterative tio understand what variable I wanted to use to get the best results for each case. By delving deep into the statistics of the players I was able appriate all my favorite players even more by understaing the crux of there playStyles.*
# NBA players Clustering/Regression Project(Based on 2020/2021 season): Overview
- Used KMeans from sklearn to cluster players to analyse similar play styles, see how good a player is, and determine if the traditional PPG, AST and RPG are good ways to jusge a player.
- Cleaned and organized data in Pandas to create the best possible Data Frame to use for exploratory data analysis and model building.
- Used Seaborn and Matplotib to determine which stats were best fit to use in our clusters and our regrassion models. 
- Created models: Multiple Linear Regression with test and train cases and determined best Height and Weight for Offensive Rebounts and Defencive rebounds in the NBA. 
- Created model the Predicts Points per game but looking at other game and pysical statistics.




## Code
**Python**: Version 3.7.6    
**Packages**: Numpy, Pandas, Kmeans, Sklearn, matplotib, selinium, seaborn   
**Tableau**: https://public.tableau.com/profile/samruth.vennapusala#!/


## Resources
**Data Acquisitions Websites:**  
https://www.basketball-reference.com/leagues/NBA_2020_totals.html  
https://www.nba.com/stats/teams/traditional/?sort=W_PCT&dir=-1  
https://www.nbastuffer.com/2020-2021-nba-player-stats/   

## Data Cleaning
We took 3 different data sets from different sources and cominded them under one dataframe With Pandas. There was a lost of cleaning to with this data set before we could proceed to the Explorotory Data Analysis, Data Clustering and our Models. We had to make sure that the Heights and weights were in the correct readable formats and got rid of all the excessive verbage. We made sure that all the numerical data was in the right forms witht he correct units. We also had to make sure the worded data was also all in the same format. There were also issues with players shoing up multiple times because they got traded half way through the season to another team. We made sure to combine the data to best represent the player. Here is the final data set the we used for the rest of our project.

https://github.com/samruthv/2021_NBAplayers_Clustering-Regression-_Project/blob/main/Data%20Cleaning/total_Stats.csv

**The Data Sets:**
[#,	Player,	Team,	GP,_x	MPG,	FGM, FGA,	FG%,	3PM,	3PA,	3P%,	FTM,	FTA,	FT%,	TOV,	PF,	ORB,	DRB,	RPG,	APG,	SPG,	BPG,	PPG,	TEAM,	AGE,	WEIGHT,	COLLEGE,	COUNTRY,	DRAFT YEAR,	DRAFT ROUND,	DRAFT NUMBER,	GP_y,	PTS,	REB,	AST,	NETRTG,	OREB%,	DREB%,	USG%,	TS%,	AST%,	HEIGHT,	Position,	SALARY]

*The '#' represents the rank of the player on their given team. This is an opinionated rank given by one of the website. The rest of the data are factual data from officaal sorces.*   


## Exploritory Data Analysis

Between all the columns of data the we aquired, we wanted to see what the relationship between all the vectors were before we got to the clustering and the modeling aspect of the project.

Firstly here are pairplots and heatplots of the different columns of data.

<p align="center">
  Heatmaps
</p>
<p align="center">
   <img src="Exploratory%20Data%20Analysis/EDA_IMAGES/Dataset1_heatmap.png" width="450" > <img src="Exploratory%20Data%20Analysis/EDA_IMAGES/Dataset2_heatmap.png" width="435"  >
</p>
<p align="center">
  Pairmaps
</p>
<p align="center">
   <img src="Exploratory%20Data%20Analysis/EDA_IMAGES/Stats_Correlation_pairplot.png" width="450" > <img src="Exploratory%20Data%20Analysis/EDA_IMAGES/DATA2_pairplots.png" width="451"  >
</p>


*Double click the maps to open the picture in a new tab to get a clearer picture*    

There is a lot to break down with these tables. There are a lot of statistics with stong positive coorilation, some with negative coorilation and some that are not coorilated at all. for example:

<p align="center">
  TOV vs APG    |     FT% vs BPG    |     3P% vs ORB
</p>
<p align="center">
  Strong Positive coorilation    |     No Coorilation    |     Slight Negative Coorilation
</p>

 

<p align="center">
   <img src="Exploratory%20Data%20Analysis/EDA_IMAGES/TOV_vs_APG.png" width="250" > <img src="Exploratory%20Data%20Analysis/EDA_IMAGES/FT%25_vs_BPG.png" width="250" > <img src="Exploratory%20Data%20Analysis/EDA_IMAGES/3P%25_VS_ORB.png" width="250" > 
</p>
 
We also looked at the physique of the players   
Height VS Weight     

<img src="Exploratory%20Data%20Analysis/EDA_IMAGES/Weight_VS_Height.png" width="250" >





    
    



## Model

## Contact Information

**Email:** samruthv@gmail.com   
**LinkedIn:** https://www.linkedin.com/in/samruthv/

