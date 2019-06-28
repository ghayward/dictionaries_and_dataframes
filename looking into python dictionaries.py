#!/usr/bin/env python
# coding: utf-8

# ### The purpose of this file is to play around with how dictionaries work in Python and how we can move between dictionaries and Pandas data frames. 

# #### 1. Making Dictionaries from Scartch with a For Loop

# In[1]:


katie_nums = {}
key = ['food','color','age']
values = ['spaghetti','red','34']
for i in range(len(key)):
    katie_nums[i] = values[i]


# In[2]:


katie_nums


# In[3]:


katie_strings = {}
key = ['food','color','age']
values = ['spaghetti','red','34']
for i in range(len(key)):
    katie_strings[key[i]] = values[i] 
#we get interger value for i to help with the loop, and use that to get the str


# In[4]:


katie_strings


# In[5]:


katie_string_dimensions = {}
key = ['food','color','age']
values = [['spaghetti', 'sushi'],['red','blue'],['34', '32']]
for i in range(len(key)):
    katie_string_dimensions[key[i]] = values[i]


# In[6]:


katie_string_dimensions


# #### 2. Moving between our dictionaries and Pandas data frames.

# In[7]:


#let's make this into a pandas data frame
import pandas as pd
ksd = pd.DataFrame.from_dict(katie_string_dimensions)


# In[8]:


ksd


# In[9]:


#let's go back to a dictionary
ksd_dict = ksd.to_dict()


# In[10]:


ksd_dict
#you can see it has some indexes now, pandas style


# In[11]:


#let's see how it changes stuff
print(katie_string_dimensions['food'])


# In[12]:


print(ksd_dict['food'])


# In[13]:


#let's see if what happens when we drill down one level
print(katie_string_dimensions['food'][0])


# In[14]:


print(ksd_dict['food'][0])


# In[15]:


#looks nice....I kind of like the way pandas gives us this useful row index number

