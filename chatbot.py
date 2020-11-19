#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## BUilding a hatbot with Deep NLP


# In[ ]:


#Importng the libraries


# In[2]:


import numpy as np
import tensorflow as tf
import re
import time


# In[ ]:


## Data Preprocessing


# In[4]:


#import the dataset
lines = open('data/movie_lines.txt', encoding = 'utf-8', errors = 'ignore').read().split('\n')

