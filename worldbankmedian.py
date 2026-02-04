#Importing file called Worldbank.xlsx using pandas
import pandas as pd
worldbank_data = pd.read_excel('WorldBank.xlsx')
print(worldbank_data)

#The goal of this project is to predict unemployment rate using GDP per capita, population density, year, and country
#But the dataset has null values in the GDP, and population density, and the unemployment rate
#Also the country is in words, and linear regression doesnt work with words hence dummy variables would be used
# Two approaching would be used to check the accuracy of the model: replacing the null values with mean, and median

#Replacing the null values in the GDP per capita column, the population density, and the unemployment rate using median
median_GDPpercapita = worldbank_data['GDP per capita (USD)'].median()
median_Popdensity = worldbank_data['Population density (people per sq. km of land area)'].median()
median_unempl = worldbank_data['Unemployment (% of total labor force) (modeled ILO estimate)'].median()

#Replacing the null values with the calculated mean values
worldbank_data['GDP per capita (USD)'] = worldbank_data['GDP per capita (USD)'].fillna(median_GDPpercapita)
worldbank_data['Population density (people per sq. km of land area)'] = worldbank_data['Population density (people per sq. km of land area)'].fillna(median_Popdensity)
worldbank_data['Unemployment (% of total labor force) (modeled ILO estimate)'] = worldbank_data['Unemployment (% of total labor force) (modeled ILO estimate)'].fillna(median_unempl)
print(worldbank_data)

#Utilizing dummy variables for the country column
dummies = pd.get_dummies(worldbank_data['Country Name'], dtype=float)
print(dummies)

#Merging the dummy table with the data set
merged_data = pd.concat([worldbank_data, dummies], axis='columns')
print(merged_data)

#Defining x and y axis
x = pd.concat([worldbank_data['GDP per capita (USD)'],
              worldbank_data['Population density (people per sq. km of land area)'],
              worldbank_data['Year'],
              dummies], axis='columns')
y = merged_data['Unemployment (% of total labor force) (modeled ILO estimate)']
print(x)
print(y)

#Importing linear regression
import sklearn.linear_model as linear_model
reg = linear_model.LinearRegression()
reg.fit(x,y)

#Prediction tests
#Question: Predict the unemployment rate of Spain in the year 2026 based on a given GDP per capita and Population Density
country = 'Spain'
row = pd.DataFrame(0, index=[0], columns=x.columns)
row.loc[0, country] = 1
row.loc[0, 'GDP per capita (USD)'] = 50000
row.loc[0, 'Population density (people per sq. km of land area)'] = 500
row.loc[0, 'Year'] = 2026

prediction1 = reg.predict(row)[0]
print(prediction1)

#Checking the score of the model
score_for_median = reg.score(x,y)
print(score_for_median)

#Train_test method
from sklearn.model_selection import train_test_split as tt
x_train, x_test, y_train, y_test = tt(x,y,test_size=0.2,random_state=42)
reg.fit(x_train,y_train)

train_score = reg.score(x_train,y_train)
test_score = reg.score(x_test,y_test) 

print(train_score)
print(test_score)
