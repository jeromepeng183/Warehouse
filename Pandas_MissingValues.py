#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[8]:


get_ipython().run_line_magic('time', 'np.arange(0,10000,dtype=int).sum()')


# In[9]:


get_ipython().run_line_magic('time', 'np.arange(0,100000,dtype=float).sum()')


# In[10]:


get_ipython().run_line_magic('time', 'np.arange(0,100000,dtype=object).sum()')


# In[5]:


df = DataFrame({'age':[20,21,23,19,22],'salary':[1500,2500,7500,3000,6000]},
               index=list('ABCDE'),
              columns=['age','salary','work'])
df


# In[8]:


df.work['B':'D']='Python'
df.work


# In[12]:


df


# In[10]:


df.isnull()


# In[13]:


df.isnull().any()


# In[14]:


sss1 = df.isnull().any(axis=1)
sss1


# In[16]:


df[sss1]


# In[17]:


df.notnull().all()


# In[18]:


df.notnull().all(axis=1)


# In[ ]:


#!!!!!!!!!!!!!!!!!!!!!!


# In[20]:


sss2 = df.notnull().all(axis=1)
df[sss2]   #delete missing values


# In[23]:


df.dropna(axis=0)


# In[22]:


df.dropna(axis=1)


# In[24]:


df.dropna(how='all')


# In[25]:


df.loc['A']=np.nan
df


# In[26]:


df.dropna(how='all')  #clean the waste


# In[27]:


df.fillna(value='Java') #fill all NAN with XXX


# In[28]:


df.fillna(method='backfill')


# In[29]:


df.fillna(method='ffill') 


# In[30]:


df


# In[31]:


df.fillna(method='ffill',inplace=True) #inplace function will overwrite the original DF


# In[32]:


df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




