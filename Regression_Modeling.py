import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as mplt 
import seaborn as sb

totalstats = pd.read_csv('total_Stats.csv')

#Model to see prediction for ORB with height and weight
model_dfc = totalstats[['ORB','HEIGHT','WEIGHT']]
dummies_dfc = pd.get_dummies(model_dfc)

from sklearn.model_selection import train_test_split

X = dummies_dfc.drop('ORB', axis =1)
y = dummies_dfc.ORB.values

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)


from sklearn.linear_model import LinearRegression
#Creating Linear Regression Model
#Predicting ORB from PPG
lr = LinearRegression()
lr.fit(x_train,y_train)
predictions = lr.predict(x_test)

print(predictions)
print(y_test)

#Test Model
lr_confidence = lr.score(x_test, y_test)
print("lr confidence", lr_confidence)

#Coefficient of determination R^2 is 31.9%


#Model to see prediction for DRB with height and weight
model_dfc = totalstats[['DRB','HEIGHT','WEIGHT']]
dummies_dfc = pd.get_dummies(model_dfc)

from sklearn.model_selection import train_test_split

X = dummies_dfc.drop('DRB', axis =1)
y = dummies_dfc.DRB.values

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)


from sklearn.linear_model import LinearRegression
#Creating Linear Regression Model
#Predicting ORB from PPG
lr = LinearRegression()
lr.fit(x_train,y_train)
predictions = lr.predict(x_test)

print(predictions)
print(y_test)

#Test Model
lr_confidence = lr.score(x_test, y_test)
print("lr confidence", lr_confidence)

#Coefficient of determination R^2 is 20.9%





#Model to see prediction for PPG with AST and RPG
model_dfc = totalstats[['PPG','AST','RPG']]
dummies_dfc = pd.get_dummies(model_dfc)

from sklearn.model_selection import train_test_split

X = dummies_dfc.drop('PPG', axis =1)
y = dummies_dfc.PPG.values

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)


from sklearn.linear_model import LinearRegression
#Creating Linear Regression Model
#Predicting ORB from PPG
lr = LinearRegression()
lr.fit(x_train,y_train)
predictions = lr.predict(x_test)

print(predictions)
print(y_test)

#Test Model
lr_confidence = lr.score(x_test, y_test)
print("lr confidence", lr_confidence)

#Coefficient of determination R^2 is 53.3%

#combining datasets