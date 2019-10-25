#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:20:37 2019

@author: agt520
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import os
plt.rcParams['font.sans-serif'] = "Arial"
plt.rcParams['font.family'] = "sans-serif"

path = '/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/gradient'
os.chdir(path)

fig = plt.figure()
ax = plt.axes(projection="3d")

df = pd.read_csv('group_map_similarities_restvstask.csv')

ax.set_xlabel('Gradient 1')
ax.set_ylabel('Gradient 2')
ax.set_zlabel('Gradient 3')

ax.set_xlim3d(-0.5,0.5)
ax.set_ylim3d(-0.5,0.5)
ax.set_zlim3d(-0.5,0.5)

for row in df.itertuples(index=True, name='Pandas'):
    ax.scatter3D(getattr(row,'Gradient1'), getattr(row,'Gradient2'), getattr(row,'Gradient3'), c=getattr(row,'Colors'), s=200)
    ax.text(getattr(row,'Gradient1')+0.03, getattr(row,'Gradient2')+0.03, getattr(row,'Gradient3')+0.03, getattr(row,'Map'))

plt.show()
fig.savefig('figures/3dplot.png') 