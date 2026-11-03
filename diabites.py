#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Implement K-Nearest Neighbors algorithm on diabetes.csv dataset. Compute confusion
# matrix, accuracy, error rate, precision and recall on the given dataset.

import pandas as pd

df = pd.read_csv('diabetes.csv')
print(df.info())
print(df.columns)


# In[2]:


print(df.isnull().sum())


# In[3]:


df.drop_duplicates()


# In[4]:


x = df.drop('Outcome', axis=1)


# In[5]:


x.head()


# In[6]:


y = df['Outcome']


# In[7]:


y.head()


# In[8]:


from sklearn.preprocessing import StandardScaler

scler = StandardScaler()


# In[9]:


from sklearn.model_selection import train_test_split

x_train,x_test, y_train,y_test = train_test_split(x,y, random_state=42, stratify=y)


# In[10]:


x_train = scler.fit_transform(x_train)
x_test = scler.transform(x_test)


# In[11]:


from sklearn.neighbors import KNeighborsClassifier


# In[12]:


model = KNeighborsClassifier(n_neighbors=5)


# In[13]:


model.fit(x_train, y_train)


# In[14]:


knn_pred = model.predict(x_test)


# In[17]:


from sklearn.metrics import (accuracy_score, precision_score, classification_report, confusion_matrix, recall_score)


# In[ ]:


print("accuracy_score : " , accuracy_score(knn_pred, y_test))
print("precision : " , precision_score(knn_pred, y_test))
print("recall : " , recall_score(knn_pred, y_test))
print("confusion matrix : \n" , confusion_matrix(knn_pred, y_test))
print("error rate : " , accuracy_score(knn_pred, y_test))
print("accuracy_score : " , accuracy_score(knn_pred, y_test))

