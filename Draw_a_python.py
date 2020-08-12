#!/usr/bin/env python
# coding: utf-8

# In[4]:


import turtle


# In[7]:


def drawSnake(rad, angle, len, neckard):
    for i in range(len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle/2)
    turtle.fd(rad)
    turtle.circle(neckard+1, 180)
    turtle.fd(rad*2/3)
    
def main():
    turtle.setup(1300, 800, 0, 0)
    pythonsize = 30
    turtle.pensize(pythonsize)
    turtle.pencolor('blue')
    turtle.seth(-40)
    drawSnake(40,80,5,pythonsize/2)
    
main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




