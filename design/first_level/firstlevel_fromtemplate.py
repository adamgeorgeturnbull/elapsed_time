#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 11:04:15 2018

@author: agt520
"""

import pandas as pd
import os
import re

# Rnumber file should be in 2 column format with order number as column 1 
# and Rnumber as column 2
# Give path to directory containing design file and Rnumber file
path = '/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/design/first_level'
os.chdir(path)

subjlist = 'Rnumbers.txt' # give name of Rnumber file
listsep = ',' # give separator in Rnumber file

# give template file (for one subject and one run)
templatefile = 'template.fsf'

# name design for output files
designname = 'N60_elapsed_time'

# give output directory for first level analysis
outputdir = '/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/output/first_level'

# give directory to save fsf files to
savedir = '/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/design/first_level/fsf_files'

# read Rnumbers into dataframe
df = pd.read_csv(subjlist,sep = listsep, header=None)
df.columns=['id', 'Rnumber']

# set up variables
runs = [1, 2, 3, 4]
sessions = [1]

# loop through participants, runs, and sessions, writing new files
for i in range(len(df)):
    order_Rnumber = "%02d_%s" % (df['id'][i], df['Rnumber'][i])
    only_Rnumber = "%s" % df['Rnumber'][i]
    for s in sessions:
        session_number = "S%d" % s
        for r in runs:
            Run_number = "Run_%d" % r
            Runjustnumber = "R%d_" % r
            with open(templatefile,'r') as file:
                ev = "%s_R%d" % (df['Rnumber'][i], r)
                filedata = file.read()
                output = "%s/%s/%s_%s_%s.feat" % (outputdir, order_Rnumber,
                                                      session_number, Run_number, 
                                                      designname)
                output = 'fmri(outputdir) "%s"' % output
                filedata = re.sub("fmri\(outputdir\).*", output, filedata)
                filedata = re.sub("[0-9]{2}_R[0-9]{4}", order_Rnumber, filedata)
                filedata = re.sub("R[0-9]{4}", only_Rnumber, filedata)
                filedata = re.sub("S[1-6]", session_number, filedata)
                filedata = re.sub("Run_[1-4]", Run_number, filedata)
                filedata = re.sub("R[1-4]_", Runjustnumber, filedata)
                filedata = re.sub("R[0-9]{4}_R[1-4]", ev, filedata)
            filename = "%s_%s_%s_%s.fsf" % (only_Rnumber, session_number, 
                                                Run_number, designname) 
            filename = os.path.join(savedir,filename)
            with open(filename,'w') as newfile:
                    newfile.write(filedata)
                