#!/bin/bash

# Attempting to use PIL's EXIF libraries for extracting
# GPS data is about as fun as pulling teeth. Plus iPhones
# appear to have a unique way of encoding GPS data that's
# making extraction difficult. Thankfully OSX comes with a
# utility 'mdls' that neatly outputs iPhone EXIF data

for file in "$@"
do
  lat=$(mdls $file | grep Latitude | awk '{print $3}')
  lng=$(mdls $file | grep Longitude | awk '{print $3}')
  echo [$lat, $lng],
done
