#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from numpy import arange, exp

import pandas as pd
from pandas import Series,DataFrame

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


aapl = pd.read_csv('E:/Python/data/AAPL.csv')
aapl


# In[3]:


aapl.dtypes


# In[4]:


aapl['Date'] = pd.to_datetime(aapl['Date'])


# In[5]:


aapl_test = aapl.set_index('Date')
aapl_test.head()


# In[6]:


aapl.dtypes


# In[7]:


start_value = aapl['Adj Close'].iloc[0]
end_value = aapl['Adj Close'].iloc[-1]
num_periods = len(aapl['Adj Close'])

display(start_value,end_value,num_periods)


# In[47]:


cagr_aapl = (end_value/start_value)**(1/num_periods)-1
cagr_aapl


# In[48]:


x= [i for i in range(300)]
exp_v = [start_value*((1+cagr_aapl)**(i-1)) for i in x]


# In[75]:


plot = plt.plot(x,exp_v)
plt.plot(aapl['Adj Close'])


# In[64]:


fig,ax=plt.subplots(figsize=(10,5))
ax.plot(aapl['Adj Close'],label='AAPL')
ax.plot(exp_v,label='f(exp)')

plt.legend()
plt.title('Bubble Test Field',fontsize=15)

plt.show()


# In[28]:


aapl['Adj Close']


# In[43]:


aapl_test['Adj Close']


# In[34]:


df_exp_v = DataFrame(exp_v[0:254],index=aapl['Date'])
df_exp_v


# In[90]:


spx = pd.read_csv('E:/Python/data/spx.csv')
spx.head()


# In[91]:


spx['Date'] = pd.to_datetime(spx['Date'])
spx_test = spx.set_index('Date')
spx_test


# In[92]:


start_spx = spx['Adj Close'].iloc[0]
end_spx = spx['Adj Close'].iloc[-1]
num_periods_spx = len(spx['Adj Close'])

display(start_spx,end_spx,num_periods_spx)


# In[93]:


cagr_spx = (end_spx/start_spx)**(1/num_periods_spx)-1
cagr_spx


# In[ ]:





# In[96]:


x= [i for i in range(300)]
exp_spx = [start_spx*((1+cagr_spx)**(i-1)) for i in x]


# In[97]:


fig,ax=plt.subplots(figsize=(10,5))

ax.plot(spx['Adj Close'],label='SPX')
ax.plot(exp_spx,label='F(exp)')

plt.legend()
plt.title('Bubble Test Field',fontsize=15)

plt.show()


# In[ ]:




