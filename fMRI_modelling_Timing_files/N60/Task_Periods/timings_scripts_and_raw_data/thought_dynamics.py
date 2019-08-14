#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 13:51:13 2019

@author: agt520
"""

import os
import pandas as pd
import numpy as np

path = '/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/fMRI_modelling_Timing_files/N60/Task_Periods/timings_scripts_and_raw_data'

os.chdir(path)

task = 'WM'

df = pd.read_csv('thoughts_vs_time_%s.csv' % task)
subj = list(set(list(df['RNUM'])))

rnum = []
time = []

for s in subj:
    tmpdf = df[df['RNUM']==s]
    tmpt = tmpdf['counter'].corr(tmpdf['Task'])
    time.append(tmpt)
    rnum.append(s)

data = list(zip(rnum, time))
out = pd.DataFrame(data, columns=['RNUM', 'timecorr'])
out['timecorr'] = np.arctanh(out['timecorr'])

out.to_csv('timecorr_%s.csv' % task)