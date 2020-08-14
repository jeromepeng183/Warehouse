#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# In[8]:


def main():
    print('This program find the real solutions to a quadratic\n')
    a,b,c=eval(input('Please enter the coefficients(a,b,c):'))
    delta=pow(b,2)-4*a*c
    if delta>=0:
        discRoot=math.sqrt(delta)
        root1=(-b+discRoot)/(2*a)
        root2=(-b-discRoot)/(2*a)
        print('\nThe solutions are:',root1,root2)
    else:
        print('The equation has no real roots')
main()


# In[ ]:





# In[ ]:





# In[15]:


def main():
    print('This program find the real solutions to a quadratic\n')
    a,b,c=eval(input('Please enter the coefficients(a,b,c):'))
    delta=pow(b,2)-4*a*c
    if delta>0:
        discRoot=math.sqrt(delta)
        root1=(-b+discRoot)/(2*a)
        root2=(-b-discRoot)/(2*a)
        print('\nThe solutions are:',root1,root2)
    else:
        if delta==0:
            root3=-b/(2*a)
            print('There is a double root at',root3)
        else:
            print('The equation has no real roots')
main()


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




