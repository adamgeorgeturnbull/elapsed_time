#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 14:04:12 2019

@author: agt520
"""

import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
from matplotlib import gridspec

path = '/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/gradient'
os.chdir(path)

df = pd.read_csv('group_map_similarities_onlinetask.csv')
df = df.sort_values('Gradient1')
df = df.reset_index(drop=True)
n = len(df)
val = [-0.03, 0.01]*(n/2)

fig = plt.figure(figsize=(8, 6))
gs = gridspec.GridSpec(3, 1)
ax0 = plt.subplot(gs[0])

ax0.set_xlim(-0.6,0.6)
ax0.get_yaxis().set_visible(False)
ax0.plot(df['Gradient1'], np.zeros_like(df['Gradient1']), 'o', c='b')
for i, txt in enumerate(df['Map']):
    if (i % 2) == 0:
        ax0.annotate(txt, (df['Gradient1'][i], 0), rotation=45, ha='left', va='bottom')
    else:
        ax0.annotate(txt, (df['Gradient1'][i], 0), rotation=-45, ha='left', va='top') 

ax1 = plt.subplot(gs[1])
ax1.set_xlim(-0.6,0.6)
ax1.get_yaxis().set_visible(False)
ax1.plot(df['Gradient2'], np.zeros_like(df['Gradient2']), 'o', c='b')
for i, txt in enumerate(df['Map']):
    if (i % 2) == 0:
        ax1.annotate(txt, (df['Gradient2'][i], 0), rotation=45, ha='left', va='bottom')
    else:
        ax1.annotate(txt, (df['Gradient2'][i], 0), rotation=-45, ha='left', va='top')
        
ax2 = plt.subplot(gs[2])
ax2.set_xlim(-0.6,0.6)
ax2.get_yaxis().set_visible(False)
ax2.plot(df['Gradient3'], np.zeros_like(df['Gradient2']), 'o', c='b')
for i, txt in enumerate(df['Map']):
    if (i % 2) == 0:
        ax2.annotate(txt, (df['Gradient3'][i], 0), rotation=45, ha='left', va='bottom')
    else:
        ax2.annotate(txt, (df['Gradient3'][i], 0), rotation=-45, ha='left', va='top')

fig.savefig('2d1dplot_onlinetask.png')   
plt.show()