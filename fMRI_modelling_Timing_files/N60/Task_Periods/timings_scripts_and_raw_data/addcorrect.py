#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 13:51:13 2019

@author: agt520
"""

import os
import pandas as pd

path = '/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/fMRI_modelling_Timing_files/N60/Task_Periods/timings_scripts_and_raw_data'

os.chdir(path)

task = 'WM'

df = pd.read_csv('MW_ratings_N61_1_session_%s_trials.csv' % task)
df['Correct'] = df['keyResp']==df['Ans']

df.to_csv('trials_with_correct_%s.csv' % task, index=False)