#!/usr/bin/env python
# coding: utf-8

# In[43]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.cm import rainbow
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns


# In[2]:


import pandas as pd


# In[3]:


df=pd.read_csv(r"C:\Users\PRITAM\Downloads\speed-dating_csv.csv")


# In[48]:


df.head()


# In[5]:


df.dtypes


# In[6]:


type(df)


# In[7]:


df.isnull().sum()


# In[8]:


df.describe()


# In[12]:


from matplotlib import pyplot as plt


# In[41]:



plt.hist(df.pref_o_attractive)


plt.xlabel("Age")
plt.ylabel("Number of People")


# From this above Histogram it can be concluded that age preference for dating falls in the range 20 to 40 years.

# In[19]:


plt.hist(df.importance_same_race)
plt.title("Preference of Race in Dating")

plt.xlabel("Scale[1-10]")
plt.ylabel("Number of People")


# From the above Histogram it can be concluded that people give less importance to Race for dating.

# In[21]:


plt.hist(df.expected_num_interested_in_me)
plt.title("Self-Confidence with Respect to Dating")

plt.xlabel("Scale[1-20]")
plt.ylabel("Number of People")


# THis Histogram plot shows that maximum number of people expect 2 to 5 people are interested on that particular individual.

# In[40]:


plt.hist(df.interests_correlate)
plt.show()


# From the above histogram it is derived that interests between two person falls in the range 0 to 0.5.That is interest rarely correlate with each other.

# In[60]:


df[['interests_correlate', 'importance_same_race', 'pref_o_attractive', 'expected_happy_with_sd_people',]].corr()  


# This analysis shows the correlation between given parameters.It shows that corralation is high and optimum in the diagonal values.Like example correlation of interests has optimum correlation with the couple expected to be happy, more the interest correlates happier the couple is.
# 

# In[68]:


sns.boxplot(x="gender", y="interests_correlate", data=df)


# from this above boxplot it can be seen that correlation of interests applies same both on male and female.
# 

# In[70]:


sns.boxplot(x="gender", y="expected_happy_with_sd_people", data=df)


# This boxplot shows that comparing two genders male are satisfied with their partner more than that of female.

# In[71]:


sns.boxplot(x="gender", y="pref_o_attractive", data=df)


# This boxplot says that female gives more preference to the trait of being attractive and looks than that of male.

# In[ ]:





# In[ ]:




