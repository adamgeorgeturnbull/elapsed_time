# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
from glob import glob
import numpy as np
import pandas as pd

task = 'WM'

path = '/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/motion'
evloc = '/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/fMRI_modelling_Timing_files/N60/Task_Periods/%s/non_target_mod/*' % task
evlist = glob(evloc)

os.chdir(path)

subjects = []
runs = []
motions = []
counters = []

for file in evlist:
    subj = file[-12:-7]
    run = file[-5]
    motionloc = '/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/output/first_level/*_%s/S1_Run_%s_N60_elapsed_time.feat/mc/prefiltered_func_data_mcf_rel.rms' % (subj, run)
    motionfile = glob(motionloc)
    if not motionfile:
        continue
    motion = np.loadtxt(motionfile[0])
    timinginfo = np.loadtxt(file)
    tr = np.floor(timinginfo[:,0]/3)
    tr = tr.astype(int)
    counter = timinginfo[:,2]
    counter = counter - min(counter)
    tr = tr[tr<179]
    counter = counter[:len(tr)]
    motion = motion[tr]
    subj = [subj] * len(counter)
    run = [run] * len(motion)
    motion = list(motion)
    counter = list(counter)
    subjects.extend(subj)
    runs.extend(run)
    motions.extend(motion)
    counters.extend(counter)
    
data_tuples = list(zip(subjects,runs,motions,counters))
df = pd.DataFrame(data_tuples, columns=['Rnum','Run','motion','counter'])
df['Task'] = '%s' % task
df.to_csv('motion_by_time_%s.csv' % task, index=False)