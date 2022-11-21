#!/usr/bin/env python
# coding: utf-8

# Data Analysis where i import the libraries and the datas

# In[98]:


import pandas as pd
import numpy as np
import plotly.express as px
import requests
import io
from datetime import date


# In[6]:


url = 'https://raw.githubusercontent.com/Marcellopp/Desarollo-de-applicaciones-mobiles/main/healthy_lifestyle_city_2021.csv?token=GHSAT0AAAAAABZYTLOLF5NFJYHJFPDWOMTUY3UWNFA'
download = requests.get(url).content


# Here i create a dataframe with the data captured

# In[78]:


df = pd.read_csv(io.StringIO(download.decode('utf-8')))
df.head()


# In[ ]:





# In[ ]:





# It's know that the more sunshine has a city the happier it is. So what is the Happiest city?

# In[70]:


df.iloc[df['Sunshine hours(City)'].argsort()[::-1][:1]]


# But is it true? which is the happiest city based on the data present in the database? 

# In[82]:


df.iloc[df['Happiness levels(Country)'].argsort()[::-1][:1]]


# No, those are not the same cities, CAIRO has a Happiness value of 4.15 compared to HELSINKI that has a 7.8

# In[ ]:





# In[ ]:





# What are the 3 bigger cities based on number of takeouts

# In[68]:


df.iloc[df['Number of take out places(City)'].argsort()[::-1][:3]]


# I need to convert the type of the data to be able to use those in an eventual comparison so i also remove symbols

# In[79]:


df['Cost of a bottle of water(City)'] = df['Cost of a bottle of water(City)'].str.lstrip('£')
df['Obesity levels(Country)'] = df['Obesity levels(Country)'].str.rstrip('%')
df['Cost of a monthly gym membership(City)'] = df['Cost of a monthly gym membership(City)'].str.lstrip('£')


# In[80]:


df['Sunshine hours(City)'] = pd.to_numeric(df['Sunshine hours(City)'], errors = 'coerce')
df['Cost of a bottle of water(City)'] = pd.to_numeric(df['Cost of a bottle of water(City)'], errors = 'coerce')
df['Obesity levels(Country)'] = pd.to_numeric(df['Obesity levels(Country)'], errors = 'coerce')
df['Pollution(Index score) (City)'] = pd.to_numeric(df['Pollution(Index score) (City)'], errors = 'coerce')
df['Annual avg. hours worked'] = pd.to_numeric(df['Annual avg. hours worked'], errors = 'coerce')
df['Cost of a monthly gym membership(City)'] = pd.to_numeric(df['Cost of a monthly gym membership(City)'], errors = 'coerce')
print(df.dtypes)


# What city is more Healhy? Comparison between Pollution and Cost of gym membership 

# In[83]:


df_new = df[['City','Pollution(Index score) (City)', 'Cost of a monthly gym membership(City)']]
df_new


# In[89]:


df_new.sort_values('Pollution(Index score) (City)')


# In[90]:


df_new.sort_values('Cost of a monthly gym membership(City)')


# We can see that the aren't strong relationships between the pollution and the cost of a gym membership also 
# because this last one depends a lot on the economy of the city itself but we can notice that the most polluted
# countriees are also beneth the poorest and so the cost of gym membership is noticable lower... 

# In[ ]:





# In[ ]:





# Relation between obesity and Life expectancy(years).

# 

# In[95]:


df_nonan = df.dropna()


# In[101]:


df_nonan.sort_values('Obesity levels(Country)')
fig = px.pie(df_nonan, values='Obesity levels(Country)', names='City', title='Obesity percentage in cities')
fig.show()


# In[ ]:





# In[103]:



df_nonan.sort_values('Life expectancy(years) (Country)')
fig = px.pie(df_nonan, values='Life expectancy(years) (Country)', names='City', title='Life expectancy(years) (Country)')
fig.show()


# In[115]:


df_ob=df_nonan.iloc[df_nonan['Obesity levels(Country)'].argsort()[:10]]
df_ob


# In[ ]:





# In[113]:


df_life=df_nonan.iloc[df_nonan['Life expectancy(years) (Country)'].argsort()[::-1][:10]]
df_life


# We notice that there is a clear relation between the obesity level anda the life expectancy, for example we can see how 5 out of 10 of the cities with lover % of obesity are present in the top 10 cities with the higher life expectancy.

# In[ ]:





# In[ ]:





# In[116]:


df_sport = df[['City','Outdoor activities(City)', 'Cost of a monthly gym membership(City)']]
df_sport


# In[117]:


df_sport.sort_values('Cost of a monthly gym membership(City)')

