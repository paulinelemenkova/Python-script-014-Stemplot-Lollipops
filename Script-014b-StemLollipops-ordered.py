#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
 
# Loading data
os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Morph.csv")
df = pd.DataFrame({'group':df.profile, 'values':df.tg_angle}) # take only two values: bath. profiles and angles
#df

# Reorder it following the values:
ordered_df = df.sort_values(by='values') # sort df by values
 
# Making the plot
markerline, stemlines, baseline = plt.stem(x, ordered_df['values'], markerfmt="o", basefmt='-')

# Setting properties
plt.setp(markerline, mfc='salmon', markersize=13, alpha=0.7, markeredgewidth=.2) 
plt.setp(stemlines, linewidth=.5, color='dimgray') 
plt.setp(baseline, color='purple', linewidth=1)
plt.suptitle('Geomorphologycal analysis of the Mariana Trench: \nSorted plot by steepness angles', fontsize=12)
plt.xlabel('Bathymetric profiles', fontsize=10, fontfamily='sans-serif')
plt.ylabel('tg$^\circ$ (A/H)', fontsize=10, fontfamily='sans-serif')
plt.show()

