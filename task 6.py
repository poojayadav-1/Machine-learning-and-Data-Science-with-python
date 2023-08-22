#!/usr/bin/env python
# coding: utf-8

# # Machine Learning for Linear Equation Prediction
# Description: You are tasked with developing a machine learning model that can predict linear
# equations based on a given dataset. The dataset consists of pairs of input variables and
# corresponding output values, representing different linear equations. Your goal is to train a
# model that can accurately predict the coefficients of a linear equation given new input values.
# 
# Requirements:
#     
# Dataset Generation:
# •Generate a dataset of multiple linear equations, each represented by a pair of input
# variables and the corresponding output value.
# •Ensure that the dataset includes a variety of linear equations with different slopes and
# intercepts.
# •You can use a random generator or predefined equations to create the dataset.
# 
# Data Pre-processing:
# •Perform any necessary pre-processing steps on the dataset, such as data normalization or
# standardization, to ensure better model performance.

# In[32]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[33]:


data = pd.read_csv("Hotel Reservations.csv")
data.head()


# In[34]:


data.info()


# In[35]:


data.dropna(inplace = True)


# In[36]:


data.info()


# In[37]:


data.hist(figsize=(20,15));


# In[38]:


data.corr()


# In[39]:


plt.figure(figsize = (15,8))
sns.heatmap(data.corr(), annot = True, cmap = "Blues_r")


# In[40]:


data['required_car_parking_space'] = np.log(data['required_car_parking_space'] + 1)
data['repeated_guest'] = np.log(data['repeated_guest'] + 1)
data['no_of_previous_cancellations'] = np.log(data['no_of_previous_cancellations'] + 1)
data['no_of_previous_bookings_not_canceled'] = np.log(data['no_of_previous_bookings_not_canceled'] + 1)
data['no_of_special_requests'] = np.log(data['no_of_special_requests'] + 1)


# In[41]:


data.hist(figsize = (20,15));


# In[42]:


data.booking_status.value_counts()


# In[43]:


plt.figure(figsize = (15,8))
sns.scatterplot(x = 'no_of_children', y = 'no_of_adults', data = data,hue = "no_of_special_requests")


# In[44]:


data['guets ratio'] = data['no_of_adults']/data['no_of_children'] 


# In[45]:


plt.figure(figsize = (15,8))
sns.heatmap(data.corr(), annot = True, cmap = "Greens_r")


# In[46]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X = data.drop(['no_of_adults'],axis = 1)
y = data['no_of_adults']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)

