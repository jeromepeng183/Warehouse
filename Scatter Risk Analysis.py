#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from numpy.random import normal, uniform
import matplotlib.pyplot as plt


# In[ ]:





# In[2]:


return1=normal(size=100)*10
risk1=uniform(0,0.5,size=100)

return2=normal(0.5,size=100)*10
risk2=uniform(0.3,1,size=100)

return3=normal(-2,size=100)*10
risk3=uniform(0,1,size=100)


# In[11]:


plt.scatter(risk1,return1)
plt.scatter(risk2,return2)
plt.scatter(risk3,return3)

plt.xlabel('Risk')
plt.ylabel('Return')


plt.show()


# In[ ]:





# In[14]:


plt.scatter(risk1,return1,label='Stock 1')
plt.scatter(risk2,return2,label='Stock 2')
plt.scatter(risk3,return3,label='Stock 3')

plt.xlabel('Risk')
plt.ylabel('Return')
plt.legend() #label

plt.show()


# In[15]:


plt.scatter(risk1,return1,label='Stock 1')
plt.scatter(risk2,return2,label='Stock 2')
plt.scatter(risk3,return3,label='Stock 3')

plt.xlabel('Risk')
plt.ylabel('Return')
plt.legend(loc='lower right') #label

plt.show()


# In[3]:


df=pd.read_csv('risk_return.csv')
df


# In[5]:


fig, ax=plt.subplots(figsize=(10,5))

ax.scatter(df['risk'],df['return'])

plt.show()


# In[ ]:





# In[15]:


fig, ax=plt.subplots(figsize=(10,5))

ax.scatter(df['risk'],df['return'])
ax.scatter(df['risk'][3],df['return'][3],color='gold',marker='*',s=300,label='Gold ETF')

plt.legend()
plt.xlabel('Risk',size=15)
plt.ylabel('Return',size=15)
plt.title('ETF',size=20)

plt.show()


# In[18]:


df


# In[ ]:





# In[28]:


fig, ax=plt.subplots(figsize=(10,5))

ax.scatter(df['risk'][0],df['return'][0],color='red',marker='o',s=300,label='0050 ETF',alpha=0.5)
ax.scatter(df['risk'][1],df['return'][1],color='blue',marker='v',s=300,label='High Div. ETF',alpha=0.5)
ax.scatter(df['risk'][2],df['return'][2],color='green',marker='8',s=300,label='Gov. ETF',alpha=0.5)
ax.scatter(df['risk'][3],df['return'][3],color='gold',marker='*',s=300,label='Gold ETF',alpha=0.5)
ax.scatter(df['risk'][4],df['return'][4],color='black',marker='h',s=300,label='Oil ETF',alpha=0.5)
ax.scatter(df['risk'][5],df['return'][5],color='purple',marker='s',s=300,label='Vix ETF',alpha=0.5)
ax.scatter(df['risk'][6],df['return'][6],color='grey',marker='*',s=300,label='EMbond ETF',alpha=0.5)
#alpha is for transparecy

plt.legend()#Icon; plt.legend(loc='lower right')
plt.xlabel('Risk',size=15)
plt.ylabel('Return',size=15)
plt.title('ETF Performance',size=20)

plt.show()


# In[ ]:





# In[31]:


fig, ax=plt.subplots(figsize=(10,5))

ax.scatter(df['risk'][0],df['return'][0],color='red',marker='o',s=300,label='0050 ETF',alpha=0.5)
ax.scatter(df['risk'][1],df['return'][1],color='blue',marker='v',s=300,label='High Div. ETF',alpha=0.5)
ax.scatter(df['risk'][2],df['return'][2],color='green',marker='8',s=300,label='Gov. ETF',alpha=0.5)
ax.scatter(df['risk'][3],df['return'][3],color='gold',marker='*',s=300,label='Gold ETF',alpha=0.5)
ax.scatter(df['risk'][4],df['return'][4],color='black',marker='h',s=300,label='Oil ETF',alpha=0.5)
ax.scatter(df['risk'][5],df['return'][5],color='purple',marker='s',s=300,label='Vix ETF',alpha=0.5)
ax.scatter(df['risk'][6],df['return'][6],color='grey',marker='*',s=300,label='EMbond ETF',alpha=0.5)
#alpha is for transparecy

plt.xlim(xmin=0,xmax=60)
plt.ylim(ymin=0)


plt.legend()#Icon; plt.legend(loc='lower right')
plt.xlabel('Risk',size=15)
plt.ylabel('Return',size=15)

plt.xticks(fontsize=13)
plt.yticks(fontsize=13)

plt.title('ETF Performance',size=20)

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





# 

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





# In[19]:


fig, ax=plt.subplots(figsize=(10,5))

ax.scatter(df['risk'],df['return'])

plt.show()


# In[ ]:





# In[19]:


fig, ax=plt.subplots(figsize=(10,5))

ax.scatter(df['risk'],df['return'])

plt.show()


# In[23]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[25]:


titanic_df = pd.read_excel('sample.xlsx')


# In[ ]:





# In[ ]:





# In[ ]:





# In[22]:


pandas.__version__


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




