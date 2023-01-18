#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os 
import csv


# In[2]:


election_csv = os.path.join ("Resources","election_data.csv")
election_csv


# In[3]:


with open(election_csv) as csv_file:
    csv_reader=csv.reader(csv_file)


# In[4]:


election_df = pd.read_csv(election_csv)


# In[5]:


election_df.head()


# In[6]:


total_votes = len(election_df)
total_votes


# In[7]:


candidates_count = election_df["Candidate"].value_counts()
candidates_count


# In[8]:


percent_candidates_count = candidates_count/total_votes*100
rounded_percent_candidates_count = round(percent_candidates_count, 3)
rounded_percent_candidates_count


# In[9]:


charles = rounded_percent_candidates_count[1]
charles


# In[10]:


diana = rounded_percent_candidates_count[0]
diana


# In[11]:


raymon = rounded_percent_candidates_count[2]
raymon


# In[12]:


max_votes = max(percent_candidates_count)
max_votes


# In[13]:


print("Election Results")
print("-------------------------")
print("Total Votes: "+ str(total_votes))
print("-------------------------")
print("Charles Casper Stockham: "+ str(charles)+"%")
print("Diana DeGette: "+ str(diana)+"%")
print("Raymon Anthony Doane: "+ str(raymon)+"%")
print("-------------------------")
print("Winner "+ str(max_votes))
print("-------------------------")


# In[ ]:




