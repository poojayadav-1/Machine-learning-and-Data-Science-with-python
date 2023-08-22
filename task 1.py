#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd


# In[9]:


sample_list=[1,2,3,4,5]
series_ls = pd.Series(sample_list)
print(series_ls)


# In[25]:


sample_dict={"Company Name":["Kia","Maruti Suzuki","Hyundai","Mahindra","Honda","Toyota"],"Model Name":["Kia Seltos","Maruti Suzuki Brezza","Hyundai Creta","Mahindra Thar","Honda City","Toyota Fortuner"],"Fuel Type":["Diesel/Petrol","Petrol/CNG","Diesel/Petrol","Diesel/Petrol","Petrol","Diesel/Petrol"],"Body Style":["SUV", "SUV","SUV","SUV","Sedan","SUV"],"Car Length":["4,315 mm", "3,995 mm","4,300 mm","3,985 mm","4,583 mm","4,795 mm"]}
df_dict = pd.DataFrame(sample_dict)


# In[26]:


print(df_dict)


# In[30]:


sample_csv = pd.read_csv("C:\\Users\\pooja yadav\\Documents\\PHN internship\\Task 2.csv")


# In[31]:


print(sample_csv)


# In[32]:


sample_excel = pd.read_excel("C:\\Users\\pooja yadav\\Documents\\PHN internship\\Task 2.xlsx")


# In[33]:


print(sample_excel)


# In[79]:


data = {'Company Name':["Kia", "Maruti Suzuki","Hyundai","Mahindra","Honda","Toyota"],
        'Model Name':["Kia Seltos","Maruti Suzuki Brezza","Hyundai Creta","Mahindra Thar","Honda City","Toyota Fortuner"],
        'Fuel Type':["Diesel/Petrol","Petrol/CNG","Diesel/Petrol","Diesel/Petrol","Petrol","Diesel/Petrol"], 
        'Body Style':["SUV","SUV","SUV","SUV","Sedan","SUV"],  
        'Car Length':["4,315 mm","3,995 mm","4,300 mm","3,985 mm","4,583 mm","4,795 mm"]}


# In[80]:


df1 =  pd.DataFrame(data, index=["0","1","2","3","4","5"])


# In[81]:


df1


# In[82]:


data = {'Company Name':["Skoda"],
        'Model Name':["Skoda"], 
        'On road pricing':["Rs.14,16,141"],   
        'Loan amount':["Rs.12,74,141"], 
        'Monthly EMI':["Rs.26,947"]}


# In[85]:


df2 = pd.DataFrame(data, index=["1"])


# In[86]:


df2


# In[90]:


df1.merge(df2, left_on="Company Name", right_on="Company Name")


# In[ ]:




