# 2021_NBAplayers_Clustering-Regression-_Project

  *As a huge fan of sports and basketball, I wanted to work on a project the involved deep numerical analysis on basketball players and teams. My goal for this project was to really dive into what separates ever player in terms or play style. This was a challenging iterative process to understand what variable to use to get the best results for each case. Furthermore, By delving deep into the statistics of the players I was able appreciate all my favorite players even more by understanding the crux of their playstyles.*
# NBA players Clustering/Regression Project (Based on 2020/2021 season): Overview
- Used KMeans from sklearn to cluster players to analyze similar play styles, see how good a player is, and determine if the traditional PPG, AST and RPG are good ways to judge a player.
- Cleaned and organized data in Pandas to create the best possible Data Frame to use for exploratory data analysis and model building.
- Used Seaborn and Matplotib to determine which stats were best fit to use in our clusters and our regression models. 
- Created models: Multiple Linear Regression with test and train cases and determined best Heights and Weights for Offensive Rebounds and Defensive rebounds in the NBA. 
- Created model the Predicts Points per game but looking at game statistics and body physique.


<p align="center">
   Mean of Some NBA Statistics
</p>

<p align="center">
   <img src="Data%20Cluster/Players_mean_stats.PNG" width="700" >
</p>



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
We took 3 different data sets from different sources and combined them under one data frame with Pandas. There was a lot of cleaning to do with this data set before we could proceed to the Exploratory Data Analysis, Data Clustering and Modeling. We had to make sure that the Heights and weights were in the correct readable formats and got rid of all the excessive verbiage. We made sure that all the numerical data was in the right forms with the correct units. We also had to make sure the worded data was also all in the same format. There were also issues with players showing up multiple times because they got traded halfway through the season to another team. We made sure to combine the data to best represent the player. Here is the final data set we used for the rest of our project.

https://github.com/samruthv/2021_NBAplayers_Clustering-Regression-_Project/blob/main/Data%20Cleaning/total_Stats.csv

**The Data Sets:**
[#,	Player,	Team,	GP,_x	MPG,	FGM, FGA,	FG%,	3PM,	3PA,	3P%,	FTM,	FTA,	FT%,	TOV,	PF,	ORB,	DRB,	RPG,	APG,	SPG,	BPG,	PPG,	TEAM,	AGE,	WEIGHT,	COLLEGE,	COUNTRY,	DRAFT YEAR,	DRAFT ROUND,	DRAFT NUMBER,	GP_y,	PTS,	REB,	AST,	NETRTG,	OREB%,	DREB%,	USG%,	TS%,	AST%,	HEIGHT,	Position,	SALARY]

*The '#' represents the rank of the player on their given team. This is an opinionated rank given by one of the websites. The rest of the data are factual data from official sources.*   


## Exploratory Data Analysis

Between all the columns of data we acquired, we wanted to see what the relationship between all the vectors were before we got to the clustering and the modeling aspect of the project.

Firstly, here are pair plots and heat plots of the different columns of data.

<p align="center">
  Heatmaps
</p>
<p align="center">
   <img src="Exploratory%20Data%20Analysis/EDA_IMAGES/Dataset1_heatmap.png" width="400" > <img src="Exploratory%20Data%20Analysis/EDA_IMAGES/Dataset2_heatmap.png" width="387"  >
</p>
<p align="center">
  Pairmaps
</p>
<p align="center">
   <img src="Exploratory%20Data%20Analysis/EDA_IMAGES/Stats_Correlation_pairplot.png" width="400" > <img src="Exploratory%20Data%20Analysis/EDA_IMAGES/DATA2_pairplots.png" width="401"  >
</p>


*Double click the maps to open the picture in a new tab to get a clearer picture*    

There is a lot to break down with these tables. There are a lot of statistics with strong positive correlation, some with negative correlation and some that are not correlation at all. for example:

<p align="center">
  TOV vs APG    |     FT% vs BPG    |     3P% vs ORB
</p>
<p align="center">
  Strong Positive Correlation    |     No Correlation    |     Slight Negative Correlation
</p>

 

<p align="center">
   <img src="Exploratory%20Data%20Analysis/EDA_IMAGES/TOV_vs_APG.png" width="250" > <img src="Exploratory%20Data%20Analysis/EDA_IMAGES/FT%25_vs_BPG.png" width="250" > <img src="Exploratory%20Data%20Analysis/EDA_IMAGES/3P%25_VS_ORB.png" width="250" > 
</p>
 
We also looked at the physique of the players.   
Height VS Weight     

<img src="Exploratory%20Data%20Analysis/EDA_IMAGES/Weight_VS_Height.png" width="250" >

## Clustering and Modeling

Our next step we performed 2 dimensional and multidimensional clustering with K-Means to see how well we can predict the original data with our model.

The first situation we were able to cluster and evaluate in tableau was our Height vs. Weight. In this model we were able to predict the position that a player played with 73.2% accuracy.

<p align="center">

<img src="Data%20Cluster/Player_Position_Predictor.PNG" width="550" >
</p>

We then move onto more complex clustering models in python. One of the situations we were trying to cluster were the type of players. This was a difficult task because we did not want k-means to cluster the players who get more playing time to less playing. If we used all the variables our model just separated the players by who put up more higher stats vs lower stats. We did not want this. What we want was to cluster by play style. So, the 'catch and shoot player', 'big man', 'facilitators', 'all rounded player’ and ect get paired, respectively. For us to get this result, we could not include any variables that were correlated to playing time (We go into more detail on why we cannot use time dependent statistics more in detail at the bottom of the 'Clustering and Modeling' section). So, for example instead of using 3 points made, we would use 3-point percentage. This was a very iterative process and I kept going back to look at where the models were placing players until I thought a model looked good enough. There is no correct or incorrect answer to this clustering as it kept changing as I was tuning the model with variables. But in the end, I was able to land on a cluster that I thought was pretty good. 



<img src="Data%20Cluster/PlayerType%20PredictiveModel.png" width="350" >


We first have the facilitators. These are the players with a high basketball IQ and can see plays happening before they happen. In addition, these types of players are typically masters of the half court set offense and they usually know the correct spots for each player on the court. It was not by coincidence that a lot of point guards or players with good assist percentages got placed in this category. 

Some Examples of **facilitators** include Chris Paul, Ben Simmons, Kemba Walker and Darius Garlang.

<p align="center">
   <img src="Data%20Cluster/Players/ChrisPaul.png" width="200" > <img src="Data%20Cluster/Players/BenSimmons.png" width="200" > <img src="Data%20Cluster/Players/KembaWalker.png" width="200" > <img src="Data%20Cluster/Players/DariusGarlang.png" width="200" > 
</p>    



Next Up we have the Big Men. This is typically a tall and physical low post player that is good with good with offensive and defensive rebounds. When someone is referring to the big man on a basketball team, they are usually referring to either the power forward or center.

Some examples of the **Big Men** include Nikola Vucevic, Kristaps Porzingis, Karl-Anthony Towns and Joel Embiid

<p align="center">
   <img src="Data%20Cluster/Players/NikolaVucevic.png" width="200" > <img src="Data%20Cluster/Players/KristapsPorzingis.png" width="200" > <img src="Data%20Cluster/Players/KarlAnthonyTowns.png" width="200" > <img src="Data%20Cluster/Players/JoelEmbied.png" width="200" > 
</p>    

We then get to the shooters, who are exactly what they sound like. High shooting rates with good finishing percentages. A shooter cannot be described by position as easily as a big man and a facilitator, there can be and are many power forwards that are considered shooters. 

Some example of **shooters** include Kyle Korver, Duncan Robinson, Joe Harris and Gordan Hayward.

<p align="center">
   <img src="Data%20Cluster/Players/KyleKorver.png" width="200" > <img src="Data%20Cluster/Players/DuncanRobinson.png" width="200" > <img src="Data%20Cluster/Players/JoeHarris.png" width="200" > <img src="Data%20Cluster/Players/GordanHayword.png" width="200" > 
</p>    

We also have a miscellaneous category that include a lot of players that do not match any of the other classifications. What I found was that a lot of these players were placed in this category because they did not have enough time played to describe there playing style correctly. For example, there was a player that had a 100% shooting percentage and a player with 0 APG. This was since they did not have enough stats to be classified properly. I had to adjust the variables and the k-means parameters to cluster these players out.

Finally, we have the all-round players. These are the players that usually do everything, and a lot of the all-star players get categorized in this category.

Some examples of the **all-round** players include Lebron James, Nikola Jokic, Jason Tatum and Kawaii Leonard.

<p align="center">
   <img src="Data%20Cluster/Players/LebronJames.png" width="200" > <img src="Data%20Cluster/Players/NikolaJokic.png" width="200" > <img src="Data%20Cluster/Players/JasonTatum.png" width="200" > <img src="Data%20Cluster/Players/KawaiiLeanord.png" width="200" > 
</p>    

I wanted to see if this model was related to the player salary in any sort of way but as I expected there was not much correlation at all 6.87%. However, I also looked at the correlation between some of the popular stats and salary and there was most definitely a correlated.

PPG vs Salary: 72.7% correlated.
AST vs Salary: 67.9% correlated.
RPG vs Salary: 48.9% correlated.

Can we define a good player and a bad player? We have the player rankings by team that were given by ESPN, what does our model say about the ranking on the teams. Can we predict what rank the player will be on their team with our model.

We first need to define what a good and bad player is. This was a lot more simpler than our previous task of defining the type of player because this can be a lot more objective. A player that plays on average 20 min and puts up on average 20 points is good while a player that plays 20 min and puts up 2 is not. We used almost all the non-categorical data we had and clustered the players with K-Means into 2 categories. This is how we got our good and bad players.

<img src="Data%20Cluster/good_bad_players.png" width="350" >

Our results are very strongly related to the rank given by ESPN. We were able to predict with 78.7% certainty.

(Just for my curiosity I also looked at the relationship between or new 'good and bad model' and height. There was a correlation of 1.9%)

Lastly, I wanted to create a model a cluster model with 3 variables, 'PPG', 'AST' and 'RPG'. The reason why I wanted to make a model with these variables was because these are the stats that are usually at the center of focus when talking about basketball. I wanted to show that with only these stats you cannot evaluate the player of the league.

<img src="Data%20Cluster/BasicModel.png" width="350" >

With this model we get that there is a 68.99% Relation between the model and the MPG (minutes played per game). Therefore, we need to use stats that are not time based and more performance based.


## Interesting Regression Models That I Wanted to Share (Bonus) :)

To quench my curiosity, I made a couple regression models which you can find in the models’ folder. I wanted to see how good of predicters some variable can be.

Linear Regression Models:    
prediction for ORB with height and weight (Coefficient of determination R^2 is 31.9%)    
prediction for DRB with height and weight (Coefficient of determination R^2 is 20.9%)     
prediction for PPG with AST and RPG (Coefficient of determination R^2 is 53.3%)     
    


## Contact Information

**Email:** samruthv@gmail.com   
**LinkedIn:** https://www.linkedin.com/in/samruthv/

