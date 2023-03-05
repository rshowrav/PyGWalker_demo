#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pygwalker as pyg


# In[2]:


url='https://www.basketball-reference.com/leagues/NBA_2022_totals.html'

list = pd.read_html(url)
df = pd.DataFrame(list[0])


# In[3]:


# Data cleanup as headers repeat and total lines not necessary under Tm Column

df = df[(df['Rk']!='Rk')&(df['Tm']!='TOT')]
df


# In[4]:


# Converting variables of interest to integers

df['STL'].astype(int)
df['BLK'].astype(int)


# In[5]:


gwalker = pyg.walk(df)

