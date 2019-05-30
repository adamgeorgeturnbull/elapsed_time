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
path = '/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/design/fixed_level'
os.chdir(path)

subjlist = 'Rnumbers.txt' # give name of Rnumber file
listsep = ',' # give separator in Rnumber file

# give template file (for one subject and all runs)
templatefile = 'template.fsf'

# name design for output files
designname = 'N60_elapsed_time'

# give output directory for fixed level analysis
outputdir = '/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/output/fixed_level'

# give directory to save fsf files to
savedir = '/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/design/fixed_level/fsf_files'

# read Rnumbers into dataframe
df = pd.read_csv(subjlist,sep = listsep, header=None)
df.columns=['id', 'Rnumber']

# loop through participants, runs, and sessions, writing new files
for i in range(len(df)):
    order_Rnumber = "%02d_%s" % (df['id'][i], df['Rnumber'][i])
    with open(templatefile,'r') as file:
        filedata = file.read()
        output = "%s/%s/%s.feat" % (outputdir, order_Rnumber, designname)
        output = 'fmri(outputdir) "%s"' % output
        filedata = re.sub("fmri\(outputdir\).*", output, filedata)
        filedata = re.sub("[0-9]{2}_R[0-9]{4}", order_Rnumber, filedata)
    filename = "%s_%s.fsf" % (order_Rnumber, designname)
    filename = os.path.join(savedir,filename)
    with open(filename,'w') as newfile:
        newfile.write(filedata)
                