#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


GOOG=pd.read_csv('GOOG.csv')
MSFT=pd.read_csv('MSFT.csv')
GOOG.set_index(pd.to_datetime(GOOG['Date'],format='%Y-%m-%d'),inplace=True)
MSFT.set_index(pd.to_datetime(MSFT['Date'],format='%Y-%m-%d'),inplace=True)

GOOG['G_pct']=(GOOG['High']-GOOG['Low'])/GOOG['Low']
MSFT['M_pct']=(MSFT['High']-MSFT['Low'])/MSFT['Low']

df=pd.merge(GOOG,MSFT,left_index=True,right_index=True,how='inner')
df=df[['G_pct','M_pct']]
df.tail()


# In[7]:


df.hist()


# In[12]:


df['G_pct'].hist()


# In[ ]:





# In[15]:


df['G_pct'].hist(bins=25) #seperate the X in 20 groups equally


# In[ ]:





# In[16]:


bins=[0,0.01,0.05,0.15]
df['G_pct'].hist(bins=bins) #seperate the X in 4 groups based on my requirement above


# In[ ]:





# In[23]:


df['G_pct'].hist(bins=20,density=True,color='skyblue',range=(0.02,0.1),cumulative=True,orientation='horizontal') #seperate the X in 20 groups equally


# In[ ]:





# In[28]:


df['G_pct'].hist(bins=20,density=True,label='GOOG')
df['M_pct'].hist(bins=20,density=True,color='orange',label='MSFT',alpha=0.5) 

plt.legend()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




