#!/bin/bash

for i in $(ls *.log*| sort -g -r); do 

  fullfilename="$i"
  filename=$(basename "$fullfilename")
  ext="${filename##*.}" 

# Check ext is integer
if [ $ext -eq $ext 2> /dev/null ]; then
  new_ext=`expr $ext + 1`
  fname="${filename%.*}"
  mv $fullfilename $fname.$new_ext

elif [ $ext = "log" ]; then
        mv $fullfilename $fullfilename.1
        touch $fullfilename
fi
done
