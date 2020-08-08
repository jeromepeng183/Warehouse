#!/usr/bin/env python
# coding: utf-8

# In[14]:


import matplotlib.pyplot as plt


# In[18]:


sales = [100,80,50]
x_labels = ['A品牌','B品牌','C品牌']
plt.bar(x_labels,sales)
plt.show()


# In[1]:


import matplotlib


# In[2]:


print(matplotlib.__file__)


# In[4]:


import matplotlib.font_manager
a = sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])

for i in a:
    print(i)


# In[ ]:


SimHei


# In[9]:


import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']


# In[10]:


sales = [100,80,50]
x_labels = ['A品牌','B品牌','C品牌']
plt.bar(x_labels,sales)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




