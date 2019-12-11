#/bin/bash

# get info of phenix.refine output
#
# C.Orr
#

# set project name
project="FutA"

# set path to processing directory
processpath=/dls/i23/data/2019/cm23006-3/processing/RUNNING/FutA

# set high and low
run_low=1
run_high=100

#####################################
# no changes below this line!!!
#####################################

mkdir $processpath/results

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
    echo "$processpath/$project_phenixref_$run exists..."
  else 
    echo "$processpath/$project_phenixref_$run doesn't exist..."
    exit 0
  fi

  cd $processpath/$project\_phenixref_$run
  echo `pwd`
  grep "^HETATM 2496" $project.pdb >> $processpath/results/randomocc.txt
  grep "^HETATM 2496" $project\_refine_001.pdb >> $processpath/results/occrefine.txt
  run=$(( $run + 1 ))
done
