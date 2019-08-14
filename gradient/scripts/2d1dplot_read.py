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

df = pd.read_csv('group_map_similarities_readvstask.csv')

fig = plt.figure(figsize=(8, 6))
gs = gridspec.GridSpec(2, 1, height_ratios=[3,1])
ax0 = plt.subplot(gs[0])

ax0.set_xlim(-0.6,0.6)
ax0.set_ylim(-0.6,0.6)

ax0.set_xlabel('Gradient 1')
ax0.set_ylabel('Gradient 2')

for row in df.itertuples(index=True, name='Pandas'):
    if getattr(row, 'Read') == 'Yes' and getattr(row, 'Rest') == 'Yes':
        ax0.scatter(getattr(row,'Gradient1'), getattr(row,'Gradient2'), c='b')
    elif getattr(row, 'Read') == 'No' and getattr(row, 'Rest') == 'Yes':
        ax0.scatter(getattr(row,'Gradient1'), getattr(row,'Gradient2'), c='r')
    elif getattr(row, 'Read') == 'Yes' and getattr(row, 'Rest') == 'No':
        ax0.scatter(getattr(row,'Gradient1'), getattr(row,'Gradient2'), c='b', marker='x')
    elif getattr(row, 'Read') == 'No' and getattr(row, 'Rest') == 'No':
        ax0.scatter(getattr(row,'Gradient1'), getattr(row,'Gradient2'), c='r', marker='x')

ax0.scatter(df.loc[df['Map']=='Reading']['Gradient1'], df.loc[df['Map']=='Reading']['Gradient2'], c='g')
ax0.annotate('Reading', (df.loc[df['Map']=='Reading']['Gradient1'], df.loc[df['Map']=='Reading']['Gradient2']), rotation=45, ha='left', va='bottom')
ax0.scatter(df.loc[df['Map']=='CRT>WM']['Gradient1'], df.loc[df['Map']=='CRT>WM']['Gradient2'], c='k')
ax0.annotate('CRT>WM', (df.loc[df['Map']=='CRT>WM']['Gradient1'], df.loc[df['Map']=='CRT>WM']['Gradient2']), rotation=45, ha='left', va='bottom')
ax0.scatter(df.loc[df['Map']=='WM>CRT']['Gradient1'], df.loc[df['Map']=='WM>CRT']['Gradient2'], c='k')
ax0.annotate('WM>CRT', (df.loc[df['Map']=='WM>CRT']['Gradient1'], df.loc[df['Map']=='WM>CRT']['Gradient2']), rotation=45, ha='left', va='bottom')

ax1 = plt.subplot(gs[1])
ax1.set_xlim(-0.6,0.6)
ax1.set_xlabel('Gradient 3')
ax1.get_yaxis().set_visible(False)

for row in df.itertuples(index=True, name='Pandas'):
    if getattr(row, 'Read') == 'Yes' and getattr(row, 'Rest') == 'Yes':
        ax1.scatter(getattr(row,'Gradient3'), 0, c='b')
    elif getattr(row, 'Read') == 'No' and getattr(row, 'Rest') == 'Yes':
        ax1.scatter(getattr(row,'Gradient3'), 0, c='r')
    elif getattr(row, 'Read') == 'Yes' and getattr(row, 'Rest') == 'No':
        ax1.scatter(getattr(row,'Gradient3'), 0, c='b', marker='x')
    elif getattr(row, 'Read') == 'No' and getattr(row, 'Rest') == 'No':
        ax1.scatter(getattr(row,'Gradient3'), 0, c='r', marker='x')

ax1.scatter(df.loc[df['Map']=='Reading']['Gradient3'], 0, c='g')
ax1.annotate('Reading', (df.loc[df['Map']=='Reading']['Gradient3'], 0), rotation=45, ha='left', va='bottom')
ax1.scatter(df.loc[df['Map']=='CRT>WM']['Gradient3'], 0, c='k')
ax1.annotate('CRT>WM', (df.loc[df['Map']=='CRT>WM']['Gradient3'], 0), rotation=45, ha='left', va='bottom')
ax1.scatter(df.loc[df['Map']=='WM>CRT']['Gradient3'], 0, c='k')
ax1.annotate('WM>CRT', (df.loc[df['Map']=='WM>CRT']['Gradient3'], 0), rotation=45, ha='left', va='bottom')

fig.savefig('2d1dplot_readvstask.png')   
plt.show()