#!/bin/bash

read -p "Enter start date (DD-MM-YYYY): " START_DATE
read -p "Enter end date (DD-MM-YYYY): " END_DATE



{
  for year_folder in ../../Module2/20*/*.txt; do
    # Start mapper.py processes
    python3 mapper.py "$year_folder" "$year_folder" &

  

  # Wait for all mapper.py processes to complete
    wait
  done
  wait
  
 } | {
    python3 reducer.py "$START_DATE" "$END_DATE" > result.txt
}