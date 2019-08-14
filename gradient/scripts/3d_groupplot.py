#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 15:43:53 2019

@author: agt520
"""

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

path = '/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/gradient'
os.chdir(path)

df = pd.read_csv('group_map_similarities.csv')

fig = plt.figure()
ax = plt.axes(projection="3d")

ax.set_xlabel('Gradient 1')
ax.set_ylabel('Gradient 2')
ax.set_zlabel('Gradient 3')

ax.set_xlim3d(-0.5,0.5)
ax.set_ylim3d(-0.5,0.5)
ax.set_zlim3d(-0.5,0.5)

for row in df.itertuples(index=True, name='Pandas'):
    ax.scatter3D(getattr(row,'Gradient1'), getattr(row,'Gradient2'), getattr(row,'Gradient3'), c='b', s=1)
    ax.text(getattr(row,'Gradient1'), getattr(row,'Gradient2'), getattr(row,'Gradient3'), getattr(row,'Map'))
    
plt.show()