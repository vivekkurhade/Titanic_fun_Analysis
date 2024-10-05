import numpy as np
import pandas as pd
import matplotlib.pyplot as pt


# Data Analysis and Visualization for Market Trends Using Python, NumPy, Pandas, and Matplotlib
titanic = pd.read_csv('titanic.csv')
print()
print("The First 5 rows are : \n\n",titanic.head(5))
print()
print("The shape is : ",titanic.shape)
print()


titanic['age'] = titanic['age'].fillna(titanic['age'].median())
titanic = titanic.drop(columns=['cabin','sibsp'])

print("The survived Candidates in the titanic : \n  ")
print(titanic.loc[titanic['survived']==1])
print()
print("The female Passengers are : \n")
print(titanic.loc[titanic['sex']=='female'])

passenger_class = titanic.groupby(['pclass']).agg(averagesales = ('fare','mean'))
print()
print("The Passenger Class and along with their average fare is : ")
print(passenger_class)
print()
print("The number of survivors based on gender are as follows : ")
gender_based_survival = titanic.groupby(['sex']).agg(Survived = ('survived','sum'))
print()
print(gender_based_survival)
print()
print("The mean age of the passengers was :",titanic['age'].mean())
print("The Median fare paid by passengers who survived are : ")

survived_people = titanic.loc[titanic['survived']==1]
print(survived_people['fare'].median())
not_survived_people = titanic.loc[titanic['survived']==0]

print("The Median fare paid by passengers who were unable to survive are : ")

print(not_survived_people['fare'].median())
