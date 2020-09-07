#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from pandas import Series,DataFrame

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


nd = np.linspace(0,100, num=50)
s = Series(nd)
s.plot()


# In[4]:


s.cumsum().plot()


# In[3]:


df = DataFrame(np.random.randint(0,30,size=(10,4)),index=list('abcdefghij'),
              columns=list('ABCD'))
df


# In[4]:


df.plot(title='DataFrame')


# In[5]:


df.plot(kind = 'bar')


# In[10]:


df.plot(kind = 'barh')


# In[6]:


nd = np.random.randint(0,5,size=10)
s=Series(nd)


# In[9]:


nd


# In[7]:


s.hist()


# In[18]:


nd1 = np.random.randint(0,50,size=(50,5))
df1=DataFrame(nd1,columns=list('XYABC'))
df1.plot(x='X',y='Y',kind='scatter')


# In[19]:


pd.plotting.scatter_matrix(df1,diagonal='kde')

