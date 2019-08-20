#!/bin/bash
#$ -o /scratch/$HOME/logs
#$ -e /scratch/$HOME/logs
#$ -N ROI_featquery
#$ -l h_vmem=32G

set -e # stop if I error
set -u # error if you call an unset (empty) variable

# Alternatively, you can create a list of zstat maps in a text file and use cat to load it.
subjdirs=`cat /scratch/groups/Projects/P1300/fMRI_data/elapsed_time/gradient/subject_level/subjectlist_elapsed_time_TT_WM.txt`

# mask to use for correlations
Mask="/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/gradient/gradient_mask.nii.gz"

#gradient maps
Grad1="/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/gradient/volume.313.1_MNI.nii.gz"
Grad2="/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/gradient/volume.313.2_MNI.nii.gz"
Grad3="/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/gradient/volume.313.3_MNI.nii.gz"

for n in $subjdirs; do
	# print the progress
	echo $n

	fsl_glm -i $n -d $Grad1 -o tmp.txt --demean -m $Mask 
	cat tmp.txt >> betas_elapsed_timeTT_WM1.txt
	fsl_glm -i $n -d $Grad2 -o tmp.txt --demean -m $Mask
	cat tmp.txt >> betas_elapsed_timeTT_WM2.txt
	fsl_glm -i $n -d $Grad3 -o tmp.txt --demean -m $Mask
	cat tmp.txt >> betas_elapsed_timeTT_WM3.txt
done

