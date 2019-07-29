#!/bin/bash
#$ -o /scratch/$HOME/logs
#$ -e /scratch/$HOME/logs
#$ -N ROI_featquery
#$ -l h_vmem=32G

set -e # stop if I error
set -u # error if you call an unset (empty) variable

# mask to use for correlations
Mask="/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/gradient/gradient_mask.nii.gz"

#gradient maps
Grad1="/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/gradient/volume.313.1_MNI.nii.gz"
Grad2="/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/gradient/volume.313.2_MNI.nii.gz"
Grad3="/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/gradient/volume.313.3_MNI.nii.gz"

#output directory
OUTPUT="/scratch/groups/Projects/P1300/fMRI_data/elapsed_time/gradient"

# Loop through leave-one-out files to create variables with lists of zstat maps.

for f in `ls /scratch/groups/Projects/P1300/fMRI_data/elapsed_time/gradient/leave_one_out/*off*.txt | sort -V`; do
	subjlists=`cat $f`
	echo $subjlists >> log_offtask.txt
	fslmerge -t merge_tmp.nii.gz $subjlists
	fslmaths merge_tmp.nii.gz -Tmean mean_tmp.nii.gz
	fslcc -m $Mask --noabs -t -1 -p 3 mean_tmp.nii.gz $Grad1 >> gradient1_offtask.txt
	fslcc -m $Mask --noabs -t -1 -p 3 mean_tmp.nii.gz $Grad2 >> gradient2_offtask.txt
	fslcc -m $Mask --noabs -t -1 -p 3 mean_tmp.nii.gz $Grad3 >> gradient3_offtask.txt
	rm *tmp*
done
