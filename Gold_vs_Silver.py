#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[17]:


SLV=pd.read_csv('Silver.csv')
SLV.set_index(pd.to_datetime(SLV['Date'],format='%Y-%m-%d'),inplace=True)
SLV.head()


# In[ ]:





# In[18]:


GLD=pd.read_csv('Gold.csv')
GLD.set_index(pd.to_datetime(GLD['Date'],format='%Y-%m-%d'),inplace=True)
GLD.head()


# In[ ]:





# In[19]:


fig,ax=plt.subplots(figsize=(10,5))
ax.plot(SLV['Adj Close'],color='skyblue',label='Silver',linestyle='--')

plt.legend()

plt.show()


# In[ ]:





# In[59]:


fig,ax=plt.subplots(figsize=(10,5))
ax.plot(SLV['Adj Close'],color='silver',label='Silver')
ax.set_ylabel('Silver',color='silver',fontsize=15)
ax.tick_params(axis='y',labelcolor='silver')
ax.legend(loc='center left')

plt.grid()


ax2=ax.twinx()
ax2.plot(GLD['Adj Close'],color='gold',label='Gold')
ax2.set_ylabel('Gold',color='gold',fontsize=15)
ax2.tick_params(axis='y',labelcolor='gold')
ax2.legend(loc='lower left')

plt.title('Gold vs Silver',fontsize=15)

plt.show()


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





# In[4]:





# In[ ]:





# In[ ]:




