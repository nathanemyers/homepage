#!/bin/bash

lat=$(mdls $1 | grep Latitude | awk '{print $3}')
lng=$(mdls $1 | grep Longitude | awk '{print $3}')
echo $lat / $lng
