#!/bin/bash

# Script to run multiple separate phenix refinements
#
# C.Orr 30/07/2019
#

# set project name
project="FutA"

# set path to processing directory
processpath=/dls/i23/data/2019/cm23006-3/processing/RUNNING/FutA/

# set high and low
run_low=1
run_high=100

######################################
# no changes below this line!!!
######################################


# load modules
module load phenix
module load global/cluster

if [ -d $processpath ]
  then
    echo
    echo "$processpath exists..."
  else
    echo "$processpath doesn't exist..."
    exit 0
fi

# 
# loop for X number of runs 
#
run=$run_low 

while [ $run -le $run_high ]
do
  if [ -d $processpath/$project\_phenixref_$run ]
  then
    echo "$processpath/$project\_phenixref_$run exists..."
  else 
    mkdir $processpath/$project\_phenixref_$run
  fi

  cd $processpath/$project\_phenixref_$run
  cp $processpath/scripts/$project\.pdb . 
  cp $processpath/scripts/$project\.mtz .
  echo `pwd`
ADPRANGE=$(shuf -i 1-100 -n 1)
OCCRANGE=$(awk -v min=0.01 -v max=0.99 'BEGIN{srand(); printf("%.2f\n", min+rand()*(max-min))}')
  phenix.pdbtools $project.pdb selection="chain 'B'" adp.set_b_iso=$ADPRANGE occupancies.set=$OCCRANGE output.file_name=$project.pdb
  qsub -P i23 -q low.q -l h_vmem=4G -pe smp 2 -cwd $processpath/scripts/phenixref_job.sh
#  $processpath/scripts/phenixref_job.sh &
 run=$(( $run + 1 ))
done

