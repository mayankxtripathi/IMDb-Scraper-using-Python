#!/usr/bin/env python
# coding: utf-8

# In[105]:


import pandas as pd   
import requests       
from bs4 import BeautifulSoup 
import numpy as np  


# In[106]:


url = 'https://www.imdb.com/search/title/?sort=user_rating,asc&groups=top_1000&count=100'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


# In[107]:


movie_name = []
year = []
time = []
rating = []
metascore = []
votes = []
gross = []
description = []
Director = []
Stars = []


# In[108]:


movie_data = soup.findAll('li', attrs= {'class': 'ipc-metadata-list-summary-item__tc'})


# In[109]:


for store in movie_data:
    name = store.a.h3.text
    movie_name.append(name)
    
  


# In[110]:


movie_DF = pd.DataFrame({'Name of movie': movie_name, 'Year of relase': year, 'Watchtime': time, 'Movie Rating': rating, 'Metascore': metascore, 'Votes': votes, 'Gross collection': gross})
 


# In[111]:


movie_DF.to_csv("Top_100_IMDB_Movies.csv", index=False)


# In[112]:


movie_DF.head(10)


# In[ ]:




