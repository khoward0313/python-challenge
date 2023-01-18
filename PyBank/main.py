#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import os 
import csv


# In[9]:


budget_csv = os.path.join ("Resources","budget_data.csv")
budget_csv


# In[10]:


with open(budget_csv) as csv_file:
    csv_reader=csv.reader(csv_file)


# In[11]:


budget_df = pd.read_csv(budget_csv)


# In[12]:


budget_df.head()


# In[13]:


total_months = (len(budget_df["Date"]))
total_months


# In[14]:


total = budget_df["Profit/Losses"].sum()
total


# In[15]:


average_change = budget_df["Profit/Losses"].mean()
average_change


# In[16]:


mtm_change = [budget_df["Profit/Losses"][i + 1] - budget_df["Profit/Losses"][i] for i in range(len(budget_df["Profit/Losses"])-1)] 
mtm_change


# In[17]:


mtm_change_max = max(mtm_change)
mtm_change_max


# In[18]:


mtm_change_min = min(mtm_change)
mtm_change_min


# In[20]:


average_mtm = sum(mtm_change)/len(mtm_change)
rounded_average = round(average_mtm,2)
rounded_average


# In[23]:


print('Financial Analysis')
print('----------------------------')
print("Total Months: " + str(total_months))
print("Total: " + "$" + str(total))
print("Average Change: " + "$" + str(rounded_average))
print("Greatest Increase in Profits " + "$" + str(mtm_change_max))
print("Greatest Decrease in Profits " + "$" + str(mtm_change_min))

