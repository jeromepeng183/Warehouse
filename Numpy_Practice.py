#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


np.__version__


# In[2]:


import matplotlib.pyplot as plt


# In[16]:


capture=plt.imread('capture.jpg')

plt.imshow(capture)
plt.show()


# In[6]:


type(capture)


# In[10]:


n2=np.array([[2,3,4,5],[3,4,5,6],[55,66,77,88]])
n2


# In[11]:


n2.shape


# In[12]:


capture.shape


# In[19]:


n3=np.array(list('1245ABC'))
n3


# In[21]:


n4=np.array([1,3,1.4,'Python'])
n4


# In[22]:


np.ones(shape=(10,8),dtype=int)


# In[23]:


ones=np.ones(shape=(100,80,3),dtype=float)


# In[24]:


plt.imshow(ones)
plt.show()  #a picture


# In[3]:


np.zeros([4,4])


# In[4]:


np.full([10,10],fill_value=1024)


# In[4]:


np.eye(10)


# In[5]:


np.linspace(0,100,20) #linear seperation from 0 to 100


# In[6]:


np.arange(0,100,20)


# In[7]:


np.random.randint(0,150,size=5)


# In[17]:


np.random.randn(100)


# In[18]:


np.random.normal(loc=170, scale=15, size=100)


# In[20]:


np.random.random(size=100)


# In[ ]:





# In[23]:


np.random.random(size=(10,10,3))


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




