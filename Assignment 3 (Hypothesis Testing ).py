#!/usr/bin/env python
# coding: utf-8

# ## HYPOTHESIS TESTING ASSIGNMENT

# ### QUESTION 1 
A F&B manager wants to determine whether there is any significant difference in the diameter of the cutlet between two units. A randomly selected sample of cutlets was collected from both units and measured? Analyze the data and draw inferences at 5% significance level. Please state the assumptions and tests that you carried out to check validity of the assumptions.


# In[74]:


import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm


# In[75]:


# Load the dataset
data=pd.read_csv("Cutlets.csv")
data.head()


# In[76]:


unitA=pd.Series(data.iloc[:,0])
unitA


# In[77]:


unitB=pd.Series(data.iloc[:,0])
unitB


# In[78]:


# 2-sample 2-tail ttest:   stats.ttest_ind(array1,array2)     # ind -> independent samples
p_value=stats.ttest_ind(unitA,unitB)
p_value


# In[84]:


pvalue=1.0    # 2-tail probability 


# In[80]:


# compare p_value with 
α = 0.05 #(At 5% significance level)


# In[86]:


# Accept Null Hypothesis
if pvalue<α:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")


# ### QUESTION 2
A hospital wants to determine whether there is any difference in the average Turn Around Time (TAT) of reports of the laboratories on their preferred list. They collected a random sample and recorded TAT for reports of 4 laboratories. TAT is defined as sample collected to report dispatch.
   
  Analyze the data and determine whether there is any difference in average TAT among the different laboratories at 5% significance level.

# In[63]:


# load the dataset
data=pd.read_csv('LabTAT.csv')
data.head()


# In[65]:


data.value_counts()


# In[67]:


# Anova ftest statistics: stats.f_oneway(column-1,column-2,column-3,column-4)
stats.f_oneway(data.iloc[:,0],data.iloc[:,1],data.iloc[:,2],data.iloc[:,3] )


# In[89]:


p__value= 2.1156708949992414e-57  
α = 0.05


# In[90]:


# Reject Null Hypothesis
if p__value<α:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")


# In[ ]:





# ### QUESTION 3 
Sales of products in four different regions is tabulated for males and females. Find if male-female buyer rations are similar across regions.
# In[24]:


import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm
from scipy.stats import chi2_contingency


# In[25]:


# load the dataset
data= pd.read_csv('BuyerRatio.csv')
data


# In[26]:


# Make dimensional array
obs=np.array([[50,142,131,70],[435,1523,1356,750]])
obs


# In[27]:


# Chi2 contengency independence test
chi2_contingency(obs) # o/p is (Chi2 stats value, p_value, df, expected obsvations)


# In[91]:


# Compare p_value with 
α = 0.05
p___value=0.6603094907091882


# In[92]:


# Accept Null Hypothesis
if p___value<α:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")


# In[ ]:





# ### QUESTION 4
TeleCall uses 4 centers around the globe to process customer order forms. They audit a certain %  of the customer order forms. Any error in order form renders it defective and has to be reworked before processing.  The manager wants to check whether the defective %  varies by centre. Please analyze the data at 5% significance level and help the manager draw appropriate inferences

# In[30]:


# load the dataset
data=pd.read_csv('Costomer+OrderForm.csv')
data


# In[37]:


data.describe()


# In[23]:


data.Phillippines.value_counts()


# In[24]:


data.Indonesia.value_counts()


# In[25]:


data.Malta.value_counts()


# In[26]:


data.India.value_counts()


# In[27]:


# Make a contingency table
obs=np.array([[271,267,269,280],[29,33,31,20]])
obs


# In[28]:


# Chi2 contengency independence test
chi2_contingency(obs) # o/p is (Chi2 stats value, p_value, df, expected obsvations)


# In[93]:


# Compare p_value with 
α = 0.05
p____value=0.2771020991233135
if p____value<α:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")


# In[ ]:





# In[ ]:




