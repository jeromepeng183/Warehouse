#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


class_1=['Finance','Industry','IT']
class_2=['Banks','Securities','Cars','Oils','Computers','5G']

val_1=[80,70,100]
val_2=[30,50,35,35,30,70]


# In[11]:


fig,ax=plt.subplots(figsize=(5,5))

ax.pie(val_1,labels=class_1,autopct='%.0f%%',radius=0.75,labeldistance=0.7, pctdistance=0.45,wedgeprops=dict(width=0.3,edgecolor='white'))
ax.pie(val_2,labels=class_2,autopct='%.0f%%',radius=1,pctdistance=0.85,wedgeprops=dict(width=0.3,edgecolor='white'))

plt.show()


# In[ ]:





# In[34]:


fig,ax=plt.subplots(figsize=(5,5))

colors=['lightblue','skyblue','lightcoral','orange','lightgreen','limegreen']

pie1,c1_text,n1_text=ax.pie(val_1,labels=class_1,autopct='%.0f%%',radius=1,labeldistance=0.53, pctdistance=0.36,wedgeprops=dict(width=0.5,edgecolor='white'))
ax.pie(val_2,labels=class_2,autopct='%.0f%%',radius=1.5,pctdistance=0.9,wedgeprops=dict(width=0.5,edgecolor='white'),colors=colors)

for t in c1_text:
    t.set_size(12)

for n in n1_text:
    n.set_size(12)

ax.set(title='class',aspect='equal')

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




