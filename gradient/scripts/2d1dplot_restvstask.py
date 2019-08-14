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

df = pd.read_csv('group_map_similarities_restvstask.csv')
df = df.sort_values('Gradient3')
df = df.reset_index(drop=True)
rest = df.loc[df['Rest']=='Yes']
task = df.loc[df['Rest']=='No']

fig = plt.figure(figsize=(8, 6))
gs = gridspec.GridSpec(2, 1, height_ratios=[3,1])
ax0 = plt.subplot(gs[0])

ax0.set_xlim(-0.6,0.6)
ax0.set_ylim(-0.6,0.6)

ax0.set_xlabel('Gradient 1')
ax0.set_ylabel('Gradient 2')

for row in rest.itertuples(index=True, name='Pandas'):
    ax0.scatter(getattr(row,'Gradient1'), getattr(row,'Gradient2'), c='r')
    ax0.text(getattr(row,'Gradient1'), getattr(row,'Gradient2'), getattr(row,'Map'), ha='left', va='bottom', rotation=45)
    
for row in task.itertuples(index=True, name='Pandas'):
    ax0.scatter(getattr(row,'Gradient1'), getattr(row,'Gradient2'), c='b')
    ax0.text(getattr(row,'Gradient1'), getattr(row,'Gradient2'), getattr(row,'Map'), ha='left', va='bottom', rotation=45)
 
ax1 = plt.subplot(gs[1])
n = len(df)
val = [-0.03, 0.01]*(n/2)
ax1.set_xlim(-0.6,0.6)
ax1.set_xlabel('Gradient 3')
ax1.get_yaxis().set_visible(False)
ax1.plot(rest['Gradient3'], np.zeros_like(rest['Gradient3']), 'o', c='r')
ax1.plot(task['Gradient3'], np.zeros_like(task['Gradient3']), 'o', c='b')
for i, txt in enumerate(df['Map']):
    if (i % 2) == 0:
        ax1.annotate(txt, (df['Gradient3'][i], 0), rotation=45, ha='left', va='bottom')
    else:
        ax1.annotate(txt, (df['Gradient3'][i], 0), rotation=-45, ha='left', va='top')

fig.savefig('2d1dplot_restvstask.png')   
plt.show()