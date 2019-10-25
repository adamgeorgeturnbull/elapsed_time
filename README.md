# elapsed_time
new project for elapsed time analysis.

NT=non-target.
TT=target.
ET=elapsed time.

fMRI design files, along with original timing files can be found in design/fMRI_timing_and_modelling. task-related thought is
originally positive (flipped for figures and description in paper). scripts for creating the elapsed time design files from the
original timing files are also located in fMRI timing and modelling. 

gradient analysis can be found in gradient. beta weights represent subject level similarities to each of the first three gradients
from Margulies et al., 2016. the scripts for this analysis are in gradient/scripts. elapsed time analyses are all negative 
associations with time. the third gradient is flipped compared to in Margulies et al., 2016, but results have been corrected to match
the gradient in this paper for final figures and analysis. 

brain figures are located in figures. gradient plots, including the 3D plot script can be found in gradient/figures. the input to this
script (group_man_similarities_restvstask.csv) includes r-values calculated using the fslcc command. 

the data used to create the final figures and perform the t-tests and univariate analyses are in group_level_data. gradient scores for 
the third gradient have been flipped to match the gradient direction in Margulies et al., 2016. the elapsed time beta weights have all 
been flipped to show increasing with time rather than decreasing. timecorr is originally on-task positive, and this has been flipped
for visualisation purposes. 

nifti files are not included for space and privacy reasons. any nifti files are available on request. the unthresholded niftis for the 
significant contrasts of interest are on NeuroVault. 
