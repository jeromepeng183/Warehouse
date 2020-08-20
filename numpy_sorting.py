#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[28]:


n1=np.array([5,4,3,1,2])
n1


# In[3]:


def sortn(nd):
    for i in range(nd.size):
        for j in range(i,nd.size):
            if nd[i] > nd[j]:
                nd[i],nd[j] = nd[j],nd[i]
    return nd


# In[4]:


sortn(n1)


# In[7]:


def sortnd(nd):
    for i in range(nd.size):
        min_index= np.argmin(nd[i:])+i
        nd[i],nd[min_index] = nd[min_index],nd[i]
    return(nd)
        


# In[8]:


sortnd(n1)


# In[24]:


n1.sort()
n1


# In[37]:


n2 = np.random.randint(0,150,size=10)
n2


# In[38]:


n2.sort()
n2


# In[39]:


n3=np.sort(n2)


# In[40]:


display(n2,n3)


# In[ ]:





# In[41]:


nd = np.random.randint(0,150,size=20)
nd


# In[45]:


np.partition(nd,-5)


# In[ ]:





# In[53]:


n4=np.partition(nd,5)[:5]


# In[55]:


n4.sort()
n4


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




