#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 10:48:23 2018

@author: agt520
"""

import re

# Get template file
template = '/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/design/group_level/template.fsf'

# give directory to save fsf files to
savedir = '/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/design/group_level/fsf_files'

# give list of copes
copes = range(1, 22)

# give thresh
thresh = 3.1

# give design
designname = 'N59_elapsed_time'

for cope in copes:
    outputdir = '/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/output/group_level/%s/cope%s_%s' % (designname, cope, (int(thresh*10)))
    filename = template.replace('template','%s_%s_%s' % (designname, cope, (int(thresh*10))))
    with open(template, 'r') as file:
        filedata = file.read()
        output = 'fmri(outputdir) "%s"' % outputdir
        filedata = re.sub("fmri\(outputdir\).*", output, filedata)
        filedata = re.sub('cope[0-9].feat', 'cope%d.feat' % cope, filedata)
        filedata = re.sub('3.1000000', '%.7f' % thresh, filedata)
    with open(filename, 'w') as newfile:
        newfile.write(filedata)
            