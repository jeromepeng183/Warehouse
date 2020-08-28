#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series,DataFrame


# In[3]:


nd = np.random.randint(0,10,size=(3,3))
nd


# In[4]:


np.concatenate((nd,nd), axis=0)


# In[12]:


np.concatenate((nd,nd), axis=1)


# In[6]:


def make_df(cols,inds):
    data = {c:[c+str(i) for i in inds] for c in cols}
    return DataFrame(data,index=inds,columns=cols)


# In[7]:


make_df(['A','B','C'],[1,2,3,4])


# In[8]:


df1 = make_df(list('AB'),[0,1])
df2 = make_df(list('AB'),[2,3])

pd.concat([df1,df2],axis=0)


# In[40]:


df3 = pd.concat([df1,df2],axis=1)
df3


# In[ ]:





# In[43]:


pd.concat([df1,df2],ignore_index=True)


# In[9]:


x = make_df(list('XY'),['a','b'])
y = make_df(list('XY'),['A','B'])

pd.concat([x,y],keys=['x','y'])


# In[ ]:





# In[10]:


df4 = make_df(list('ACD'),[0,1,2])
df5 = make_df(list('CDF'),[3,4,5])


# In[13]:


pd.concat([df4,df5])


# In[11]:


pd.concat([df4,df5],join_axes=[df5.columns])


# In[17]:


df6 = DataFrame({'Employee':['Paul','Sara','Dannis'],
                'Group':['Sale','Accounting','Marketing']})
df7 = DataFrame({'Employee':['Paul','Sara','Dannis'],
                'Working_Hours':[2,3,1]})
display(df6,df7)


# In[18]:


pd.merge(df6,df7)


# In[ ]:





# In[21]:


df8 = DataFrame({'Employee':['Paul','Sara','Dannis'],
                'Group':['Sale','Accounting','Marketing'],
                'Salary':[10000,8000,9000]})
df9 = DataFrame({'Employee':['Paul','Dora','Dannis'],
                'Group':['Sale','Accounting','Marketing'],
                'Work_Time':[2,1,3]})
display(df8,df9)


# In[22]:


pd.merge(df8,df9)


# In[31]:


pd.merge(df8,df9,on='Employee')


# In[ ]:





# In[30]:


pd.merge(df8,df9,on='Group')


# In[32]:


pd.merge(df8,df9,on='Group',suffixes=['A','B'])


# In[ ]:





# In[34]:


df10 = DataFrame({'Employee':['Paul','Sara','Dannis'],
                'Group':['Sale','Accounting','Marketing'],
                'Salary':[10000,8000,9000]})
df11 = DataFrame({'Employee':['Paul','Dora','Dannis'],
                'Team':['Sale','Accounting','Marketing'],
                'Work_Time':[2,1,3]})
display(df10,df11)


# In[36]:


pd.merge(df10,df11,left_on='Group',
    right_on='Team')


# In[37]:


pd.merge(df10,df11, how='outer')


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




