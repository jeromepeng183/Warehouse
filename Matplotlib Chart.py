#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


sales = [100,80,50]
x_labels = ['A','B','C']

plt.bar(x_labels,sales)


# In[6]:


sales = [100,80,50]
x_labels = ['A','B','C']

plt.barh(x_labels,sales)


# In[7]:


sales = [100,80,50]
x_labels = ['A','B','C']

plt.bar(x_labels,sales,color=['red','blue','green'])


# In[8]:


sales = [100,80,50]
x_labels = ['A','B','C']

plt.bar(x_labels,sales,color=['red','blue','green'],edgecolor="black")


# In[9]:


products=['A','B','C','D']
revenue=[20,50,40,70]


# In[16]:


plt.pie(revenue,labels=products,autopct='%.0f%%')
plt.show()


# In[ ]:





# In[17]:


plt.pie(revenue,labels=products,autopct='%.2f%%')
plt.show()


# In[ ]:





# In[20]:


plt.pie(revenue,labels=products,autopct='%.0f%%',radius=1.5)
plt.show()


# In[ ]:





# In[21]:


plt.pie(revenue,labels=products,autopct='%.0f%%',colors=['blue','red','green','brown'])
plt.show()


# In[ ]:





# In[23]:


products=['A','B','C','D']
revenue=[20,50,40,70]
colors=['blue','red','green','brown']


# In[24]:


plt.pie(revenue,labels=products,autopct='%.0f%%',colors=colors)
plt.show()


# In[ ]:





# In[25]:


products=['A','B','C','D']
revenue=[20,50,40,70]
explode=[0,0,0,0.1]


# In[30]:


plt.pie(revenue,labels=products,autopct='%.0f%%',radius=1.5,explode=explode,shadow=True)
plt.show()


# In[ ]:





# In[33]:


products=['A','B','C','D']
revenue=[20,50,40,70]
revenue_2019=[30,100,20,70]
explode=[0,0,0,0.1]


# In[36]:


fig,axis=plt.subplots(1,2)
axis[0].pie(revenue,labels=products,autopct='%.0f%%',radius=1,explode=None,shadow=True)
axis[0].set_title('2018')
axis[1].pie(revenue_2019,labels=products,autopct='%.0f%%',radius=1,explode=None,shadow=True)
axis[1].set_title('2019')

plt.show()


# In[3]:


import pandas as pd


# In[6]:


excel_file = 'revenue.xls'
revenue=pd.read_excel(excel_file)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[40]:





# In[ ]:




