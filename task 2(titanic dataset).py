#!/usr/bin/env python
# coding: utf-8

# # 1. Prepare the Titanic dataset file (download it from Google)

# In[1]:


import pandas as pd


# In[2]:


titanic_data = pd.read_csv("C:\\Users\\pooja yadav\\Documents\\PHN internship\\titanic dataset.csv")


# # 2. Find out the names of passengers younger than 35 years. 

# In[3]:


print(titanic_data.head())


# In[4]:


ages = titanic_data["Age"]


# In[5]:


print(ages.head())


# In[6]:


print(type(ages))


# In[7]:


ages_35= titanic_data[titanic_data["Age"]<35]


# In[8]:


print(ages_35)


# In[9]:


print(ages_35.shape)


# In[10]:


ages_35_1 = titanic_data["Age"]<35


# In[11]:


print(ages_35_1)


# # 3. Print the rows from index 10 to 25 and columns 3 to 5

# In[12]:


titanic_data.iloc[10:26, 2:5]


# # 4. Find out the statistics aggregate of Age & Fare using the DataFrame.agg() method

# In[13]:


titanic_data["Age"].mean()


# In[14]:


titanic_data[["Age", "Fare"]].median()


# In[15]:


titanic_data[["Age", "Fare"]].describe()


# In[16]:


titanic_data.agg(
    {
        "Age": ["min", "max", "median", "skew"],
        "Fare": ["min", "max", "median", "mean"],
    }
)


# # 5. Find out the mean ticket fare price for each of the sex and cabin class combinations

# In[17]:


titanic_data.groupby(["Sex", "Pclass"])["Fare"].mean()


# In[67]:


#It is done by groupby() method.

