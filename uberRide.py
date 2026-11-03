#!/usr/bin/env python
# coding: utf-8

# In[223]:


'''
Predict the price of the Uber ride from a given pickup point to the agreed drop-off location.
Perform following tasks:
1. Pre-process the dataset.
2. Identify outliers.
3. Check the correlation.
4. Implement linear regression and random forest regression models.
5. Evaluate the models and compare their respective scores like R2, RMSE,
'''


import pandas as pd
get_ipython().system('pip install matplotlib')
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:





# In[ ]:





# In[224]:


df = pd.read_csv("uber.csv")


# In[225]:


df.head()


# In[226]:


print(df.info())


# In[227]:


print(df.isnull().sum())


# In[228]:


df = df.dropna()


# In[229]:


print(df.isnull().sum())


# In[230]:


# calculate distance using Euclidean formula
df['distance'] = (((df['pickup_latitude'] - df['dropoff_latitude'])**2 + (df['pickup_longitude'] - df['dropoff_longitude'])**2)**0.5)


# In[231]:


sns.boxplot(x = df['passenger_count'])


# In[232]:


# calculate fare, passenger count and distance


df = df[(df['passenger_count'] > 0) & (df['passenger_count'] < 6)]
df = df[(df['fare_amount'] > 0) & (df['fare_amount'] < 100)]
df = df[(df['distance'] < 5)]
sns.boxplot(x=df['distance'])


# In[233]:


sns.boxplot(x=df['fare_amount'])


# In[234]:


sns.boxplot(x=df['passenger_count'])


# In[235]:


df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])


# In[236]:


df['hours'] = df['pickup_datetime'].dt.hour
df['hours']


# In[237]:


df['day'] = df['pickup_datetime'].dt.day_of_week
df['day']


# In[238]:


corr = df[['fare_amount', 'passenger_count', 'distance', 'hours', 'day']].corr()


# In[239]:


corr


# In[240]:


sns.heatmap(corr, annot=True, cmap='coolwarm')


# In[241]:


get_ipython().system('pip install scikit-learn')


# In[242]:


from sklearn.model_selection import train_test_split


# In[243]:


X = df[['passenger_count', 'distance', 'hours', 'day']]


# In[244]:


X


# In[245]:


Y = df['fare_amount']


# In[246]:


Y


# In[247]:


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


# In[248]:


X_train


# In[249]:


from sklearn.linear_model import LinearRegression


# In[250]:


lr = LinearRegression()


# In[251]:


linear_pred = lr.fit(X_train, Y_train)
#trained model


# In[252]:


linear_Y = linear_pred.predict(X_test)


# In[253]:


from sklearn.metrics import root_mean_squared_error, r2_score


# In[254]:


lr_rmse = root_mean_squared_error(Y_test, linear_Y)
lr_rmse


# In[255]:


r2_lr = r2_score(Y_test, linear_Y)
r2_lr


# In[256]:


from sklearn.ensemble import RandomForestRegressor


# In[257]:


rf = RandomForestRegressor(random_state=42, n_estimators=100)


# In[258]:


train_rf = rf.fit(X_train, Y_train)


# In[260]:


rf_pred = train_rf.predict(X_test)


# In[261]:


rf_pred


# In[262]:


rf_rsme = root_mean_squared_error(Y_test, rf_pred)
rf_rsme


# In[263]:


rf_r2 = r2_score(Y_test, rf_pred)
rf_r2


# In[ ]:




