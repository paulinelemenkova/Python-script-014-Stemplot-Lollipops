#!/usr/bin/env python
# coding: utf-8
#
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
#
# load data
os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Morph.csv")
x=df.profile
values=df.tg_angle
#
# stem function
markerline, stemlines, baseline = plt.stem(x, values, markerfmt="o", basefmt='-')
# setting properties
plt.setp(markerline, mfc='salmon', markersize=13, alpha=0.7, markeredgewidth=.2)
plt.setp(stemlines, linewidth=.5, color='dimgray')
plt.setp(baseline, color='purple', linewidth=1)
plt.suptitle('Geomorphologycal analysis of the Mariana Trench: \nSteepness angle by profiles', fontsize=12)
plt.xlabel('Bathymetric profiles', fontsize=10, fontfamily='sans-serif')
plt.ylabel('tg$^\circ$ (A/H)', fontsize=10, fontfamily='sans-serif')
plt.show()
plt.savefig("MyPlot.png", dpi=300)
