#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


import os
os.path.exists('Capture.jpg')


# In[10]:


capture = plt.imread('Capture.jpg')
plt.imshow(capture)


# In[11]:


capture1 = capture[::-1]
plt.imshow(capture1)


# In[15]:


capture2 = capture[::-1,::-1]
plt.imshow(capture2)


# In[16]:


capture3=capture[::,::,::-1]
plt.imshow(capture3)


# In[ ]:





# In[2]:


import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import matplotlib.pyplot as plt


# In[9]:


nd = np.array([55,4,5,2,3,7])
nd[2]


# In[10]:


s = Series(nd)
s


# In[11]:


s.index = list('abcdef')
s


# In[12]:


s1 = Series(nd, index=['a','b','c','d','e','f'])
s1


# In[13]:


s2 = Series({'a':1,'b':2,'c':3})
s2


# In[15]:


s2.iloc[0]


# In[16]:


s1.loc['a':'e']


# In[17]:


s1[0:3]


# In[6]:


df = pd.read_csv('C:/Users/jerom/MSFT.csv')
df


# In[7]:


type(df)


# In[12]:


Close_price=df['Adj Close']
Close_price


# In[11]:


type(Close_price)


# In[14]:


Close_price.head(10)


# In[15]:


Close_price.tail()


# In[21]:


ss1 = Series([5,5,5,5],index=[0,1,2,3])
ss2 = Series([6,6,6,6],index=[2,3,4,5])


# In[22]:


ss1+ss2 


# In[23]:


ss1.add(ss2)


# In[25]:


ss1.add(ss2,fill_value=0)


# In[3]:


df1 = DataFrame({'height':[175,180,165,168],
                  'age':np.random.randint(18,25,size=4),
                  'gender':['M','M','F','F']},index= list('ABCD'))
df1


# In[3]:


df1 = DataFrame({'height':[175,180,165,168],
                  'age':np.random.randint(18,25,size=4),
                  'gender':['M','M','F','F']},index= list('ABCD'),
               columns=['height','age','gender','weight'])
df1


# In[6]:


df1 = DataFrame({'height':[175,180,165,168],
                  'age':np.random.randint(18,25,size=4),
                  'gender':['M','M','F','F'],
                 'weight':[140,160,115,120]},index= list('ABCD'),
               columns=['height','age','gender','weight'])
df1


# In[20]:


df1['height']  #locating columns


# In[21]:


df1.loc['A'] #locating index 


# In[22]:


df1.loc['A','B']


# In[23]:


df1.loc[['A','B']]


# In[24]:


df1.loc['A':'C']


# In[10]:


df1.values[1,3]


# In[11]:


df2 = DataFrame(np.random.randint(80,150,size=(4,4)),
               index=['Amy','Bob','Cathy','David'],
               columns=['English','Math','Python','History'])
df2


# In[12]:


df3 = DataFrame(np.random.randint(0,150, size=(5,4)),
                index=['Amy','Bob','Cathy','David','Emma'],
                columns=['English','Math','Python','History'])
df3


# In[13]:


df2+df3


# In[16]:


df4= df2.add(df3,fill_value=0)
df4


# In[ ]:





# In[17]:


df5 = DataFrame(np.random.randint(0,150, size=(5,3)),
                index=['Amy','Bob','Cathy','David','Emma'],
                columns=['Math','Python','History'])
df5


# In[19]:


df6 = DataFrame(np.random.randint(0,150, size=(4,4)),
                index=['Amy','Bob','Cathy','David'],
                columns=['English','Math','Python','History'])
df6


# In[22]:


df7= df5.add(df6,fill_value=0)
df7


# In[23]:


df7['English'].loc['Emma']


# In[24]:


df7['English'].loc['Emma']=109


# In[25]:


df7


# In[26]:


ss1=df7['Python']
ss1


# In[27]:


ss1+df7


# In[28]:


ss2 = df7.loc['Cathy']
ss2


# In[29]:


df7+ss2


# In[30]:


ss3 = df7.loc['David']


# In[31]:


df7.add(ss3)


# In[34]:


ss4 = df7.Python
ss4


# In[39]:


df7.add(ss4,axis=0)


# In[37]:


df7


# In[40]:


df7.add(ss4,axis='index')


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





# In[7]:





# In[ ]:





# In[ ]:





# In[ ]:




