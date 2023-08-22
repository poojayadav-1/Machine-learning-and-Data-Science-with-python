#!/usr/bin/env python
# coding: utf-8

# # 1. Write a Python code to Create a figure with 2x2 subplots.

# In[181]:


import matplotlib.pyplot as plt


# In[182]:


import numpy as np


# In[183]:


#2. In the first subplot (top-left), plot a bar chart using the following data:
#Categories: ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
#Values: [23, 56, 41, 62, 19]
plt.subplot(2,2,1)
Categories= np.array(['Category A','Category B','Category C','Category D','Category E'])
Values= np.array([23, 56, 41, 62, 19])
plt.bar(Categories, Values, color= 'm')
plt.ylabel('Values')
plt.xlabel('Categories')
plt.title('Bar chart')
plt.xticks(rotation=15, fontsize=7)


#3. In the second subplot (top-right), plot a histogram using the following data:
#Data: [12, 17, 21, 18, 14, 13, 16, 9, 12, 15, 19, 11, 14, 16, 20, 18, 15, 13, 16, 11, 10]
plt.subplot(2,2,2)
Data= np.random.normal([12, 17, 21, 18, 14, 13, 16, 9, 12, 15, 19, 11, 14, 16, 20, 18, 15, 13, 16, 11, 10])
print(Data)
plt.hist(Data, color='y')
plt.title('Histogram')


#4. In the third subplot (bottom-left), plot a pie chart using the following data:
#Labels: ['Apple', 'Banana', 'Orange', 'Mango']
#Sizes: [30, 25, 15, 30]
plt.subplot(2,2,3)
Sizes= np.array([30, 25, 15, 30])
Labels= np.array(['Apple', 'Banana', 'Orange', 'Mango'])
plt.pie(Sizes, labels= Labels)
plt.title('Pie chart', y=-0.3)

#5. In the fourth subplot (bottom-right), plot a scatter plot using the following data:
#X values: [1, 2, 3, 4, 5]
#Y values: [2, 5, 3, 6, 4]
plt.subplot(2,2,4)
X = np.array([1,2,3,4,5])
Y = np.array([2,5,3,6,4])
plt.scatter(X, Y, color='g')
plt.title('Scatter plot', y=-0.3)

plt.show()

#6. Add appropriate titles and labels to each subplot.
#7. Adjust the spacing between subplots to avoid overlapping.

