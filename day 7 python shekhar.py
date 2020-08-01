#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Day7 assignment- shekhar suman


# In[2]:


#question


# In[3]:


#Use the dictionary, port1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}, and make a new dictionary in which keys become values and values become keys, as shown: Port2 = {“FTP":21, "SSH":22, “telnet":23, "http": 80}


# In[4]:


portA = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}
portB = {values:keys for keys,values in portA.items()}
print("PortB=",portB)


# In[5]:


#Take a list of tuple as shown below. [(1,2), (3,4), (5,6),(4,5)] Generate a new list which contains sum of number of tuples. For example give Input [(1,2), (3,4), (5,6)] Output [3, 7, 11]


# In[6]:


ReqList = [(1,2), (3,4), (5,6),(4,5)] 
result = []
for each in range(0,len(ReqList)):
    a,b = ReqList[each]
    result.append(a+b)
print("Output",result)


# In[7]:


#Take a list as  [(1,2,3), [1,2], ['a','hit','less']] The List contains tuple and lists. Make the elements of inner lists and tuples to outer list


# In[8]:


Lista = [(1,2,3), [1,2], ['a','hit','less']] 
Listb = []
Listb = [r for each in Lista for r in each]
print("Output - ",Listb)


# In[ ]:




