#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pandas import Series,DataFrame

import numpy as np


# In[2]:


s = Series((np.random.randint(0,100,size=4)), index=[['a','a','b','b'],['term1','term2','term1','term2']])
s


# In[43]:


df = DataFrame(np.random.randint(0,150,size=(6,3)),
               columns =['English','Math','Python'],
              index = [['Ada','Ada','Bob','Bob','Cici','Cici'],['Mid','End','Mid','End','Mid','End']])
df


# In[4]:


df1 = DataFrame(np.random.randint(70,150,size=(6,3)),columns = ['Java','C++','Python'],
               index = pd.MultiIndex.from_arrays([['Ada','Ada','Bob','Bob','Coco','Coco'],['Mid','End','Mid','End','Mid','End']]))
                
df1


# In[ ]:





# In[5]:


df2 = DataFrame(np.random.randint(70,150,size=(6,3)),columns = ['Java','C++','Python'],
               index = pd.MultiIndex.from_tuples([('Ada','Mid'),('Ada','End'),('Bob','Mid'),('Bob','End'),('Coco','Mid'),('Coco','End')]))
                
df2


# In[ ]:


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# In[6]:


df3 = DataFrame(np.random.randint(70,150,size=(6,3)),columns = ['Java','C++','Python'],
               index = pd.MultiIndex.from_product([['Ada','Bob','Coco'],['Mid','End']]))
                
df3


# In[ ]:


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# In[19]:


df4 = DataFrame(np.random.randint(70,150,size=(3,6)),
                columns = pd.MultiIndex.from_product([['Java','C++','Python'],['Mid','End']]),
               index = ['Ada','Bob','Coco'])
                
df4


# In[ ]:





# In[63]:


s


# In[64]:


s['b','term2']


# In[68]:


s[['a','b']]


# In[69]:


s['a':'b']


# In[3]:


s.iloc[0:3]


# In[7]:


df1


# In[13]:


df1['Ada':'Bob']


# In[14]:


df1.iloc[0:2]


# In[18]:


df1.loc['Bob'].loc['End']


# In[ ]:





# In[20]:


df4


# In[21]:


df4.stack()


# In[36]:


df4.stack(level=-2)


# In[37]:


df2


# In[46]:


df2.unstack(level=0)


# In[45]:


df2.unstack(level=1)


# In[47]:


df1


# In[48]:


df1.sum()


# In[49]:


df1.sum(axis=0)


# In[50]:


df1.sum(axis=1)


# In[51]:


df1.std()


# In[52]:


df1.std(axis=1)


# In[57]:


df1.max()


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




