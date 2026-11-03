#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_csv('emails.csv')


# In[4]:


print(df.info())
print(df.head(10))
print(df.isnull().sum())


# In[5]:


df.drop_duplicates()


# In[15]:


x = df.iloc[:,1:-1]


# In[16]:


y = df['Prediction']


# In[17]:


print(x)
print(y)


# In[35]:


from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from sklearn.metrics import (
accuracy_score,
f1_score,
precision_score,
confusion_matrix,
recall_score
)


# In[36]:


x_train, x_test,y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42, stratify=y)


# In[37]:


from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline


# In[38]:


# kneaighbour

k_model = KNeighborsClassifier()


# In[39]:


K_train = k_model.fit(x_train, y_train)


# In[40]:


k_pred = K_train.predict(x_test)


# In[41]:


print(k_pred)
print(y_test.head())


# In[42]:


print("accuracy score : ",accuracy_score(y_test, k_pred))


# In[43]:


print("F1 score : ",f1_score(y_test, k_pred))


# In[44]:


# precision_score,
# confusion_matrix,
# recall_score
from sklearn.metrics import classification_report
print("precision score : ",precision_score(y_test, k_pred))
print("confusion matrix : ",confusion_matrix(y_test, k_pred))
print("recall score : ",recall_score(y_test, k_pred))
print("classification report : \n",classification_report(y_test, k_pred))


# In[46]:


svc = SVC(kernel='linear')
svc.fit(x_train, y_train)
svc_pred = svc.predict(x_test)


# In[47]:


print("precision score : ",precision_score(y_test, svc_pred))
print("confusion matrix : ",confusion_matrix(y_test, svc_pred))
print("recall score : ",recall_score(y_test, svc_pred))
print("classification report : \n",classification_report(y_test, svc_pred))


# In[48]:


print("Accuracy score : ",accuracy_score(y_test, svc_pred))


# In[ ]:




