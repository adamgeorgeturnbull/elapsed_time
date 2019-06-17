#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 11:04:59 2019

@author: agt520
"""

import pandas as pd
import numpy as np

task = 'CRT' # CRT or WM
path = '/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/fMRI_modelling_Timing_files/N60/Task_Periods/timings_scripts_and_raw_data/MW_ratings_N61_1_session_%s_trials.csv' % task

df = pd.read_csv(path)

df['counter'] = ''
ct = []
counter = 0
for index, row in df.iterrows():
    last = index-1
    if index == 0:
        counter = 0
        start = df.at[index, 'stimStart_offset']
    elif index != 0 and df.at[index, 'RUN'] != df.at[last, 'RUN']:
        counter = 0
        start = df.at[index, 'stimStart_offset']
    elif index != 0 and df.at[index, 'stimStart_offset'] - df.at[last, 'stimStart_offset'] > 30:
        counter = 0
        start = df.at[index, 'stimStart_offset']
    elif df.at[index-1, 'stimType']=='TT':
        counter = 0
        start = df.at[index, 'stimStart_offset']
    else:
        counter = df.at[index, 'stimStart_offset'] - start
    ct.append(counter)

df['counter'] = ct
        
df.to_csv('trials_with_moderators_%s.csv' % task)
        
runs = list(df['RUN'])
runs = list(set(runs))
Rnum = list(df['RNUM'])
Rnum = list(set(Rnum))
    
base = '/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/fMRI_modelling_Timing_files/N60/Task_Periods/%s/non_target' % task
for run in runs:
    for R in Rnum:
        filename = base + '/%s_%s.txt' % (R, run)
        x = df[(df['RUN'] == run) & (df['RNUM'] == R) & (df['stimType'] == 'NT')]
        x = x[['stimStart_offset', 'stimT']]
        x['ones'] = int(1)
        np.savetxt(filename, x.values, fmt=['%.8f', '%.2f', '%d'])
        
base = '/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/fMRI_modelling_Timing_files/N60/Task_Periods/%s/target' % task
for run in runs:
    for R in Rnum:
        filename = base + '/%s_%s.txt' % (R, run)
        x = df[(df['RUN'] == run) & (df['RNUM'] == R) & (df['stimType'] == 'TT')]
        x = x[['stimStart_offset', 'stimT']]
        x['ones'] = int(1)
        np.savetxt(filename, x.values, fmt=['%.8f', '%.2f', '%d'])
        
base = '/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/fMRI_modelling_Timing_files/N60/Task_Periods/%s/non_target_mod' % task
for run in runs:
    for R in Rnum:
        filename = base + '/%s_%s.txt' % (R, run)
        x = df[(df['RUN'] == run) & (df['RNUM'] == R) & (df['stimType'] == 'NT')]
        x = x[['stimStart_offset', 'stimT', 'counter']]
        mc = x['counter'] - np.mean(x['counter'])
        x['counter'] = mc
        np.savetxt(filename, x.values, fmt=['%.8f', '%.2f', '%.8f'])
        
base = '/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/fMRI_modelling_Timing_files/N60/Task_Periods/%s/target_mod' % task
for run in runs:
    for R in Rnum:
        filename = base + '/%s_%s.txt' % (R, run)
        x = df[(df['RUN'] == run) & (df['RNUM'] == R) & (df['stimType'] == 'TT')]
        x = x[['stimStart_offset', 'stimT', 'counter']]
        mc = x['counter'] - np.mean(x['counter'])
        x['counter'] = mc
        np.savetxt(filename, x.values, fmt=['%.8f', '%.2f', '%.8f'])
