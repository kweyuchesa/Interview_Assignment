#!/usr/bin/env python
# coding: utf-8

# In[4]:


#importing pandas to read csv
import pandas as pd
import pandas_profiling


# In[5]:


df = pd.read_csv("Assignment.csv")
#printing out our dataset
df.sample(5)


# In[6]:


pandas_profiling.ProfileReport(df)


# In[ ]:




