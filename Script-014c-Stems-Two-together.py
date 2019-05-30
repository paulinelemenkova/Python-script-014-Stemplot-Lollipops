#!/usr/bin/env python
# coding: utf-8

# In[111]:


# libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import pylab as plt

# define figure
fig = plt.figure()
st = fig.suptitle('Geomorphologycal analysis of the Mariana Trench: 25 bathymetric profiles \nunsorted (A) and sorted (B) plots by steepness angles', 
             fontsize=12)
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

#def get_axis_limits(ax, scale=1.1):
 #   return ax.get_xlim()[1]*scale, ax.get_ylim()[1]*scale

# define subplot 1
plt.subplot(2, 1, 1)
os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Morph.csv")
x=df.profile
values=df.tg_angle
markerline, stemlines, baseline = plt.stem(x, values, markerfmt="o", basefmt='-')
plt.setp(markerline, mfc='salmon', markersize=13, alpha=0.7, markeredgewidth=.2) 
plt.setp(stemlines, linewidth=.5, color='dimgray') 
plt.setp(baseline, color='purple', linewidth=1)
plt.xlabel('Bathymetric profiles', fontsize=10, fontfamily='sans-serif')
plt.ylabel('tg$^\circ$ (A/H)', fontsize=10, fontfamily='sans-serif')

# define subplot 2
plt.subplot(2, 1, 2)
os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Morph.csv")
df = pd.DataFrame({'group':df.profile, 'values':df.tg_angle}) # take only two values: bath. profiles and angles
ordered_df = df.sort_values(by='values') # sort df by values
markerline, stemlines, baseline = plt.stem(x, ordered_df['values'], markerfmt="o", basefmt='-')
plt.setp(markerline, mfc='salmon', markersize=13, alpha=0.7, markeredgewidth=.2) 
plt.xticks( x, ordered_df['group'])
plt.setp(stemlines, linewidth=.5, color='dimgray') 
plt.setp(baseline, color='purple', linewidth=1)
plt.xlabel('Bathymetric profiles', fontsize=10, fontfamily='sans-serif')
plt.ylabel('tg$^\circ$ (A/H)', fontsize=10, fontfamily='sans-serif')

# labels
ax1.annotate('(A)', xy=(1.02, .90), xycoords="axes fraction")
ax2.annotate('(B)', xy=(1.02, .90), xycoords="axes fraction")
# 0,0 is lower left of axes and 1,1 is upper right

# plotting
plt.subplots_adjust(hspace=.2)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




