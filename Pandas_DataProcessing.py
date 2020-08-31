#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from pandas import Series,DataFrame


# In[3]:


df = DataFrame(np.random.randint(1,3,size=(5,3)),
              columns=['English','Math','English'],
              index=['Ada','Bob','Cici','Dick','Emma'])
df


# In[3]:


df.duplicated()


# In[4]:


df.drop_duplicates()


# In[5]:


df1 = pd.concat([df,df],axis=1)
df1


# In[6]:


df1.drop_duplicates()


# In[9]:


#!!!!!!!!!!!!!!!!!!!!!!! To create a new Column
df2 = DataFrame(np.random.randint(0,100,size=(3,1)),
               index=['Ada','Bob','Cici'],
               columns=['Python'])
df2


# In[14]:


def State(i):
    if i < 60:
        return 'Failed'
    elif i > 90:
        return 'Excellent'
    else:
        return 'Pass'


# In[16]:


df2['State']=df2['Python'].map(State)
df2


# In[22]:


index={'Ada':'A','Bob':'B'}
columns={'State':'Grade'}


# In[23]:


df2.rename(index=index, columns=columns)


# In[ ]:





# In[4]:


df3 = DataFrame(np.random.randint(0,100,size=(6,3)),
               index = list('ABCDEF'),
               columns = ['Math','English','Python'])
df3


# In[5]:


df3.describe()


# In[27]:


df3.std()


# In[28]:


df3.std(axis=1)


# In[31]:


df4 = np.abs(df3)>df3.std()*3
df4


# In[33]:


df5= df4.any(axis=1)
df5


# In[35]:


df3


# In[36]:


df3[df5] #pick up the outstanding ones


# In[ ]:





# In[37]:


df6 = np.abs(df3)<df3.std()*3
df6


# In[45]:


df7 = df6.all(axis=1)
df7


# In[46]:


#pick up the normal series

df3[df7]


# In[ ]:





# In[6]:


df3


# In[8]:


per = np.random.permutation(6)
per


# In[12]:


df3.take(per)


# In[ ]:





# In[13]:


df4 = DataFrame({'item':['Apple','Banana','Orenge','Banana','Orenge','Apple'],
                'price':[4,3,3,2.5,4,2],
                'color':['red','yellow','orenge','yellow','green','green']})
df4


# In[17]:


df4.groupby('item')


# In[15]:


g = df4.groupby('item')
g.groups


# In[18]:


mean = g['price'].mean()
mean


# In[19]:


df_mean = DataFrame(mean)
df_mean


# In[20]:


df_mean.columns = ['price_mean']


# In[23]:


pd.merge(df4,df_mean,left_on = 'item',right_index=True)


# In[ ]:





# In[28]:


df4.groupby('color').mean()


# In[30]:


df4.groupby(['item','color']).mean()


# In[ ]:





# In[32]:


df5 = DataFrame({'item':['radish','cabbage','pepper','melon','cabbage','pepper','melon','cabbage'],
                'color':['red','white','green','green','white','red','green','green'],
                'weight': np.random.randint(5,20,size=8),
                'price':np.random.randint(1,4,size=8)})
df5


# In[51]:


df5.groupby('color')


# In[52]:


df5.groupby('color')['price'].sum()


# In[48]:


df5.groupby('color')['price'].sum()['white']


# In[53]:


df5.groupby('item')[['weight','price']].sum()


# In[ ]:





# In[55]:


df5.groupby('item')[['weight','price']].apply(sum)


# In[56]:


df5.groupby('item')[['weight','price']].apply(max)


# In[ ]:





# In[57]:


df5.groupby('item')[['weight','price']].transform(sum)


# In[ ]:





# In[ ]:




