#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Implement K-Means clustering/ hierarchical clustering on sales_data_sample.csv dataset.
# Determine the number of clusters using the elbow method.


# In[3]:


import pandas as pd

df = pd.read_csv("sales_data_sample.csv", encoding = 'latin1')


# In[6]:


print(df.head())
print(df.columns)
print(df.isnull().sum())


# In[8]:


num_cols = df[['QUANTITYORDERED', 'PRICEEACH', 'SALES']].columns


# In[109]:


x = df[num_cols]
x


# In[11]:


from sklearn.preprocessing import StandardScaler

sc = StandardScaler()


# In[12]:


x = sc.fit_transform(x)


# In[15]:


from sklearn.cluster import KMeans

emc = []


# In[16]:


for i in range (1, 11):
    km = KMeans(n_clusters=i, random_state=42, n_init=10)
    km.fit(x)
    emc.append(km.inertia_)


# In[17]:


import matplotlib.pyplot as plt


# In[108]:


plt.plot(range(1,11), emc, marker = 'o')
plt.grid(True)
plt.xticks(range(1,11))


# In[20]:


# Hence k = 4 elbow


# In[94]:


k = 3
km = KMeans(n_clusters=k, random_state=42, n_init=10)
pred = km.fit_predict(x)


# In[ ]:





# In[95]:


df["kmeans"] = pred


# In[96]:


df


# In[97]:


get_ipython().system('pip install scipy')


# In[98]:


from scipy.cluster.hierarchy import linkage, dendrogram, fcluster


# In[99]:


linked = linkage(x, method='ward')


# In[100]:


plt.figure(figsize=(16,9))
dendrogram(linked, orientation='top', distance_sort='descending', show_leaf_counts=True)
plt.show()


# In[101]:


df['Hier_cluster'] = fcluster(linked, k, criterion='maxclust')


# In[102]:


df.head()


# In[103]:


df['Hier_cluster'] = fcluster(linked, k)
df.head()


# In[104]:


dendrogram(linked, p = 30)
plt.show()


# In[105]:


import seaborn as sns
from sklearn.cluster import AgglomerativeClustering
hierarchical = AgglomerativeClustering(
    n_clusters=k,
    linkage="ward"
)

label = hierarchical.fit_predict(x)


# In[106]:


df['cluster'] = label

plt.scatter(df['QUANTITYORDERED'],
            df['SALES'],
               c = df['cluster'],
                cmap= 'viridis',

    s=50)


# In[ ]:





# In[ ]:





# In[ ]:




