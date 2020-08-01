#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Day3 Assignment -shekhar suman


# In[3]:


#question 1 


# In[5]:


#Generate Sum of n number using while loop


# In[9]:



Number=6
if Number < 0:
    print("Enter the digit greater than Zero")
else:
    Sum=0
    while (Number > 0):
        Sum=Sum+Number
        Number=Number-1
    print("The sum of the number is",Sum)


# In[10]:


#To find out whether prime or not


# In[11]:


Number=10
i=1
if Number>1:
    if Number%i ==0:
        print("Number is not prime",Number)
    else:
        print("Number is prime",Number)
else: 
    print("Number is not prime",Number)


# In[ ]:




