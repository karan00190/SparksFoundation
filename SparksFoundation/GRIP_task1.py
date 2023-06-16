# -*- coding: utf-8 -*-
"""Spark-Task1 (Prediction on supervised learning).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1exj_HBLaZ7DAqfo1GW7krg2b2SuL4Nwl

Step 1 : Importing the libraries and datasets
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

url = "http://bit.ly/w-data"   # Data that i have opted for
ds=pd.read_csv(url)
print("Data imported successfully")
ds.head(25)

from pandas.core.describe import describe_numeric_1d

ds.tail()   # To display the bottom most records

ds.info()  # To find the category of data and other information

ds.describe()   #To analyze the statistical funtions

ds.isnull().sum()      #To check whether data contains null or missing value

"""Step 2 : Data Visualization

To plot the dataset and check the relation between the parameters

"""

plt.rcParams['figure.figsize']= [10,5]
ds.plot(x= 'Hours', y='Scores', style='+',color='blue', markersize=10)
plt.title('Hours vs Percentage')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Scored')
plt.grid()
plt.show()

ds.plot.pie(x="Hours", y="Scores")

ds.plot.scatter(x="Hours", y="Scores",color="red")

ds.plot.bar(x="Hours", y="Scores",color="lightgreen")

ds.sort_values(["Hours"], axis=0, ascending=[True],inplace=True)
ds.head(10)
ds.plot.bar(x="Hours", y="Scores",color="purple")

"""Step 3 : Data Preparation
Dividing the variables into attributes and labels
"""

x= ds.iloc[:,:1].values
y=ds.iloc[:,1:].values

y

#Splitting the data into tarin and test data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test =train_test_split(x,y,test_size=0.2, random_state=0)

"""Step 4 : Training the algorithm

Now after Splitting , finally it's time to train our algorithm

"""

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train , y_train)

print("Training Complete")

# Visualizing the model
# Plotting the regression line

line = model.coef_*x+model.intercept_

# Plotting the test data

plt.rcParams['figure.figsize']=[10,5]
plt.scatter(x,y,color='purple')
plt.plot(x,line, color='green')
plt.xlabel=("Percentage scored by student")
plt.ylabel=("Hours studied by student")
plt.grid()
plt.show()

"""Step 5 : Prediction process



"""

print(x_test)
y_pred=model.predict(x_test)
print("The predicted score based on testing data is ", y_pred)

model.score(x_test,y_test)

y_test

y_pred

df=pd.DataFrame({'Actual':[y_test],'Predicted':[y_pred]})
df

#predicting our own data

hours = 9.25
own_pred = model.predict([[hours]])
print("No. of hours = {}".format([[hours]]))
print("Predicted score = {}".format(own_pred[0]))

"""Step 6 : Evaluating the model

This is the last step i.e evaluating the performance of algorithm
For this we have used mean square method.
"""

from sklearn import metrics
print('Mean Absolute Error', metrics.mean_absolute_error(y_test,y_pred))