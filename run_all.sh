#!/usr/bin/bash

input="10_std_tail_10eVthreshold"

mkdir -p "../"$input"/hepmc"

#loop over inputs
for i in `ls ../$input/?????.csv`
do
  echo $i

  #output name from the input
  out=${i#"../$input/"}
  out="../$input/hepmc/"${out%".csv"}".hepmc"
  #echo $out

  #run the conversion
  ./build/convert_sr -i $i -o $out --invert_z 1

done 


