# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 10:14:21 2018

@author: agt520
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rc('font', family = 'Arial')
import seaborn as sns
import numpy as np
from matplotlib.ticker import FormatStrFormatter

variable1 = 'Gradient3NTET'
variable2 = 'timecorr_offtask'

file = "*insert_path*/elapsed_time_09_09.csv"

sns.set(font_scale=1.5)   
sns.set_style("white",{"font.sans-serif": "Arial"})

df = pd.read_csv(file)
df = df.replace(to_replace=" ", value=np.nan)
df.dropna(subset=[variable1], inplace=True)
df.dropna(subset=[variable2], inplace=True) 

X = df[variable1]
Y = df[variable2]

fig = plt.figure(figsize=(8,6))
ax = sns.regplot(x=pd.to_numeric(X), y=pd.to_numeric(Y), color='black')
ax.set(xlabel="Gradient 3 similarity", ylabel="Increase in off-task thought over time")
sns.despine(top=True, right=True)
ax.set_ylim(-0.5, 0.6)
ax.set_xlim(-0.7,0.25)
ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

fig.savefig("U:/Desktop/gradient/figures/plots/%s_%s.png"
            % (variable1,variable2), dpi = 300)