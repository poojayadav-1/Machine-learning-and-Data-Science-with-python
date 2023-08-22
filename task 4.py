#!/usr/bin/env python
# coding: utf-8

# # Write a Python program using NumPy to perform the following tasks on a given array:

# In[69]:


import numpy as np


# # 1. Create a NumPy array with the following values: [1, 2, 3, 4, 5].

# In[70]:


a = np.array([1,2,3,4,5])


# In[71]:


print(a)


# # 2. Print the shape of the array using the .shape attribute.

# In[72]:


print(a.shape)


# # 3. Reshape the array into a 2D array with 2 rows and 3 columns.

# In[73]:


b= np.array([(1,2,3),(3,4,5)])


# In[74]:


print(b)


# # 4. Print the shape of the new array.

# In[75]:


print(b.shape)


# # 5. Create a second NumPy array with the following values: [6, 7, 8, 9, 10].

# In[76]:


c = np.array([6,7,8,9,10])


# In[77]:


print(c)


# In[78]:


print(c.shape)


# # 6. Concatenate the two arrays together horizontally.

# In[79]:


np.hstack((a,c))


# # 7. Print the resulting array.

# In[80]:


print(np.hstack((a,c)))


# # 8. Compute the resulting array's mean, median, and standard deviation.

# In[81]:


r1 = np.mean(np.hstack((a,c)))


# In[82]:


print("\nMean: ", r1)


# In[83]:


r2 = np.median(np.hstack((a,c)))


# In[84]:


print("\nMedian: ", r2)


# In[85]:


r3 = np.std(np.hstack((a,c)))


# In[86]:


print("\nstd: ", r3)

