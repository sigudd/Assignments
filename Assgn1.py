#!/usr/bin/env python
# coding: utf-8

# In[3]:


print("jupyter Notebook installed")


# In[4]:


fname=input("Please enter your First name:")
lname=input("Please enter your Last name:")
s=(fname+" "+lname)
s[::-1]


# In[5]:


num=[]
for val in range(2000,3200):
   if (val%7==0) and (val%5!=0):
    num.append(str(val))
print (','.join(num))


# In[6]:


diameter=12
radius=diameter/2
volume=(4/3)*(3.14)*(radius**3)
print(volume)


# In[ ]:




