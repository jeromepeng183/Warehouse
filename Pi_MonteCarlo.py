#!/usr/bin/env python
# coding: utf-8

# In[3]:


from random import random
from math import sqrt
from time import process_time


# In[31]:


Darts= 1200000
hits= 0
process_time()

for i in range(1,Darts):
    x,y= random(), random()
    dist = sqrt(pow(x,2)+pow(y,2))
    if dist <=1:
        hits=hits+1
pi=4*(hits/Darts)

print('Pi value %s' %pi)
print('processing time %ss'%process_time())
    


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





# In[6]:


pow(2,2)


# In[ ]:





# In[8]:


DARTS = 12000
hits = 0
process_time()
for i in range(1, DARTS):
    x,y = random(), random()
    dist = sqrt(pow(x,2) + y**2)
    if dist<=1.0:
        hits = hits +1
    pi = 4* (hits/DARTS)
    print('Pi value %s' %pi)
    print ('time of process %-5.5ss'% process_time())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




