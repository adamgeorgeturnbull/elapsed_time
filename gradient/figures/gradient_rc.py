#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:30:07 2019

@author: agt520
"""

import pandas as pd
from numpy.random import rand
import matplotlib.pyplot as plt
from matplotlib import gridspec

grad = 3

file = '/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/gradient/figures/betas_grad%s.csv' % grad

df = pd.read_csv(file)
n = len(df)

fig = plt.figure(figsize=(8, 2))
gs = gridspec.GridSpec(1, 1)
ax0 = plt.subplot(gs[0])

ax0.set_xlim(-0.25,0.25)
ax0.get_yaxis().set_visible(False)
ax0.plot(df['Offtask'], rand(n), 'o', c='b')
ax0.plot(df['Ontask'], rand(n), 'o', c='r')
ax0.plot(df['DecreasingNT'], rand(n), 'o', c='g')

plt.show()