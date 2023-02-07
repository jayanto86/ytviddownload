#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pip install pytube')
from pytube import YouTube
link = input("Enter the link ")
print("Downloding...")
YouTube(link).streams.first().download()
print("Video downloaded successfully")


# In[ ]:

# In[ ]:
