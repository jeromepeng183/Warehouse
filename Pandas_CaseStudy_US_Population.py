#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series,DataFrame


# In[9]:


state_abbrv = pd.read_csv('E:/Python/data/State_Abbrev.csv')
state_abbrv.head()
state_abbrv = state_abbrv[['state','abbreviation']]


# In[11]:


state_area = pd.read_csv('E:/Python/data/State_Aera.csv')
state_area = state_area[['state','area (sq. mi)']]


# In[12]:


state_ppl = pd.read_csv('E:/Python/data/State_Population.csv')
state_ppl = state_ppl[['state/region','ages','year','population']]


# In[13]:


display(state_abbrv.tail(),state_area.head(),state_ppl.head())


# In[21]:


pop = pd.merge(state_ppl,state_abbrv,left_on='state/region',right_on='abbreviation',how = 'outer')
pop.shape


# In[22]:


pop


# In[24]:


pop.drop('abbreviation',axis=1, inplace=True)


# In[25]:


pop


# In[26]:


pop.isnull().any()


# In[27]:


pop['state'].isnull()


# In[29]:


df_lost = pop.loc[pop['state'].isnull()]
df_lost


# In[30]:


df_lost['state/region'].unique()


# In[31]:


state_abbrv.state


# In[32]:


pop['state/region'] == 'PR'


# In[33]:


pr = pop['state/region'] == 'PR'


# In[34]:


pop['state'][pr] = 'Puerto Rico'


# In[38]:


pop['state'][pr]


# In[39]:


usa = pop['state/region'] == 'USA'


# In[40]:


pop['state'][usa] = 'USA'


# In[41]:


pop['state'][usa]


# In[42]:


pop.isnull().any()


# In[45]:


pop2 = pd.merge(pop,state_area,how = 'left')
pop2


# In[46]:


pop2.isnull().any()


# In[47]:


pop2["area (sq. mi)"].isnull()


# In[49]:


pop2['state'][pop2["area (sq. mi)"].isnull()]


# In[51]:


pop3 = pop2.dropna()
pop3


# In[52]:


pop3.shape


# In[53]:


pop3.isnull().any()


# In[72]:


pop_2010 = pop3.query("year == '2010' & ages == 'total'")
pop_2010


# In[74]:


pop_2010.set_index('state',inplace=True)


# In[77]:


pop_density = pop_2010['population']/pop_2010["area (sq. mi)"]
pop_density.head()


# In[78]:


pop_density.sort_values(ascending=False)


# In[81]:


pop_density.sort_values(ascending=True)[0:5]


# In[85]:


pop_d = DataFrame(pop_density,columns=['pop_density'])
pop_d


# In[86]:


pd.merge(pop3,pop_d,left_on='state',right_index=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




