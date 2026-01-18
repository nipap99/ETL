#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

#Read excel
employees = pd.read_excel("H+ Sport Employees.xlsx", sheet_name="Employees-Table")

#print employees table before droping values
employees

#print  employees columns
employees.columns

#Columns to remove
columns_to_remove = ['Job Rating', 'New Salary','Tax Rate', '2.91%']
#Drop values
employees = employees.drop(columns=columns_to_remove)

#print employees table
employees

#print final employees columns
employees.columns


# In[ ]:




