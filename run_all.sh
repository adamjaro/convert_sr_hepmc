#!/usr/bin/bash

#loop over inputs
for i in `ls ../input/?????.csv`
do
  echo $i

  #output name from the input
  out=${i#"../input/"}
  out="../hepmc/"${out%".csv"}".hepmc"

  #run the conversion
  ./build/convert_sr -i $i -o $out

done 


