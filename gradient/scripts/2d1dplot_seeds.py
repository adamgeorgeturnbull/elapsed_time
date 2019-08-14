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

df = pd.read_csv('group_map_similarities_seeds.csv')
df = df.sort_values('Gradient1')
df = df.reset_index(drop=True)

fig = plt.figure(figsize=(8, 6))
gs = gridspec.GridSpec(2, 1, height_ratios=[3,1])
ax0 = plt.subplot(gs[0])

ax0.set_xlim(-0.6,0.6)
ax0.set_ylim(-0.6,0.6)

ax0.set_xlabel('Gradient 1')
ax0.set_ylabel('Gradient 2')

for row in df.itertuples(index=True, name='Pandas'):
    if getattr(row, 'Seed') == 'DMN':
        ax0.scatter(getattr(row,'Gradient1'), getattr(row,'Gradient2'), c='#cd3e4e')
    elif getattr(row, 'Seed') == 'DAN':
        ax0.scatter(getattr(row,'Gradient1'), getattr(row,'Gradient2'), c='#00760e')
    else:
        ax0.scatter(getattr(row,'Gradient1'), getattr(row,'Gradient2'), c='k')
 
ax0.annotate('Online', (df.loc[df['Map']=='Offtask']['Gradient1'], df.loc[df['Map']=='Offtask']['Gradient2']), rotation=45, ha='left', va='bottom')

ax1 = plt.subplot(gs[1])
n = len(df)
val = [-0.03, 0.01]*(n/2)
ax1.set_xlim(-0.6,0.6)
ax1.set_xlabel('Gradient 3')
ax1.get_yaxis().set_visible(False)

for row in df.itertuples(index=True, name='Pandas'):
    if getattr(row, 'Seed') == 'DMN':
        ax1.scatter(getattr(row,'Gradient3'), 0, c='#cd3e4e')
    elif getattr(row, 'Seed') == 'DAN':
        ax1.scatter(getattr(row,'Gradient3'), 0, c='#00760e')
    else:
        ax1.scatter(getattr(row,'Gradient3'), 0, c='k')
        
ax1.annotate('Online', (df.loc[df['Map']=='Offtask']['Gradient3'], 0), rotation=45, ha='left', va='bottom')

fig.savefig('2d1dplot_seed.png')   
plt.show()