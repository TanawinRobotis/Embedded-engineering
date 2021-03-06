# -*- coding: utf-8 -*-
"""Polynomial Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V-1arwAkTiQL5NCzKj_IDuYxwavQOCgT
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
# %config InlineBackend.figure_format='retina'

url = 'https://github.com/prasertcbs/basic-dataset/raw/master/worldbank_gdp_gini_birth_death_rate.csv'

data=pd.read_csv(url)

data.sample(10)

data.info()

"""**1.1 filter and visualize country data**"""

data[data['country'].str.contains('Thailand')]

x_col = 'year'
y_col = 'Death rate, crude (per 1,000 people)'
country = 'Thailand'

df = data[data['country']==country].copy()
df

sns.lmplot(x=x_col,y=y_col,data=df,fit_reg=True,
           scatter_kws={'alpha': .2,'color':'green'},
           line_kws={'color':'salmon'});

import sklearn as sk
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

x = df[[x_col]]
y = df[[y_col]]

test_size=.2
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=test_size,random_state=1)

"""**Linear regression**"""

lm = LinearRegression()
lm

lm.fit(x_train,y_train)

lm.score(x_train,y_train)

lm.coef_

lm.intercept_

lm.score(x_test,y_test)

fig=plt.figure(figsize=(10,6))
plt.scatter(x,y,color='green',alpha=.2)
plt.plot(x,lm.predict(x), color = 'red',alpha=.5)
plt.title('Linear Regression')
plt.xlabel(x_col)
plt.ylabel(y_col)

lm.predict([[1990],[2021]])

"""**Polynomial Regression**"""

poly_reg = PolynomialFeatures(degree=6)

poly_reg.fit_transform([[1990]])

v = 1990
v**0,v**1,v**2

x_train_poly = poly_reg.fit_transform(x_train)
x_test_poly  = poly_reg.fit_transform(x_test)

pm = LinearRegression()
pm.fit(x_train_poly,y_train)

pm.score(x_train_poly, y_train)

pm.intercept_

pm.coef_

pm.score(x_test_poly, y_test)

pm.predict(x_train_poly[:3])

fig=plt.figure(figsize=(10,6))
plt.scatter(x,y,color='green',alpha=.2)
plt.plot(x,pm.predict(poly_reg.fit_transform(x)), color = 'red',alpha=.5)
plt.title('Polynomial Regression')
plt.xlabel(x_col)
plt.ylabel(y_col)

fig=plt.figure(figsize=(8*2,5))
d = {'Linear Regression':lm.predict(x),
     'Polynomial Regression':pm.predict(poly_reg.fit_transform(x))}
i = 1
for title, y_pred in d.items():
  fig.add_subplot(1,2,i)
  plt.scatter(x,y,color='green',alpha=.2)
  plt.plot(x,y_pred,color ='red',alpha=.5)
  plt.title(title)
  plt.xlabel(x_col)
  plt.ylabel(y_col)
  i+=1

