#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from numpy.fft import fft,ifft

from PIL import Image


# In[2]:


Capt = Image.open('Capture.JPG')


# In[5]:


Capt


# In[6]:


capt_data= np.fromstring(Capt.tobytes(),dtype=np.int8)


# In[7]:


capt_data


# In[8]:


capt_data_fft = fft(capt_data)
capt_data_fft


# In[9]:


np.where(np.abs(capt_data_fft)<1e5,0,capt_data_fft)


# In[ ]:


capt_data_fft[np.where(np.abs(capt_data_fft)<1e5)]=0


# In[10]:


capt_data_ifft = ifft(capt_data_fft)
capt_data_ifft


# In[11]:


capt_data_real= np.real(capt_data_ifft)


# In[12]:


capt_data_real


# In[13]:


capt_data_result=np.int8(capt_data_real)


# In[14]:


capt_data_result


# In[15]:


capt_Image = Image.frombytes(size = Capt.size,mode=Capt.mode, data = capt_data_result)


# In[16]:


capt_Image


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




