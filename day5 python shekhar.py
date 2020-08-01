#!/usr/bin/env python
# coding: utf-8

# In[1]:


# day 5 assignment - shekhar suman
#question1


# In[2]:


#generate the sort in the increasing order, but all zeros should be at the right side


# In[3]:



Listinc = [0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
Listinc.sort()
c=Listinc.count(0)
print(Listinc[c:]+Listinc[:c])


# In[4]:


#merge the list using sort when two lists are given


# In[5]:


listA=[1,5,3,2,4]
listB=[7,10,8,6,9]
listC=listA+listB
listD=[]
for num in range(min(listC),max(listC)+1):
    if num in listC:
        listD.append(num)
print(listD)


# In[ ]:




