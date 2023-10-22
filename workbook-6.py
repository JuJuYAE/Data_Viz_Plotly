#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd 
import numpy as np 


# In[46]:


from plotly import __version__


# In[47]:


print(__version__)


# In[48]:


import cufflinks as cf


# In[49]:


from plotly.offline import download_plotlyjs , init_notebook_mode , plot , iplot


# In[50]:


init_notebook_mode(connected = True)


# In[51]:


cf.go_offline()


# In[52]:


#DATA 
df = pd.DataFrame(np.random.randn(100,4), columns = "A B C D".split())


# In[53]:


df.head()


# In[54]:


df2 = pd.DataFrame({"Category" : ["A", "B", "C"], "Values" : [32,43,50]})


# In[55]:


df2.head()


# In[56]:


df.iplot()


# In[57]:


df.iplot(kind = "scatter", x = "A" , y = "B", mode = "markers", color = "blue", size = 10)


# In[58]:


df2.iplot(kind = "bar", x = "Category" , y = "Values")


# In[59]:


df.iplot(kind = "box")


# In[60]:


df3 = pd.DataFrame({'x':[1,2,3,4,5],'y':[10,20,30,20,10],'z':[5,4,3,2,1]})


# In[61]:


df3.head()


# In[62]:


df3.iplot(kind = "surface")


# In[63]:


df["A"].iplot(kind = "hist" , bins = 30)


# In[64]:


df.iplot(kind = "hist")


# In[65]:


df[["A" ,"B"]].iplot(kind = "spread")


# In[66]:


df.iplot(kind = "bubble", x = "A" , y = "B", size = "C")


# In[67]:


df.scatter_matrix()


# In[ ]:





# In[ ]:




