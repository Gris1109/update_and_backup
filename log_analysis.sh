#!/bin/bash

LOG_FILE="backup.log"

# Define keywords to search for
KEYWORDS=("error" "failed" "denied" "warning")

# Search for keywords in log file
for keyword in "${KEYWORDS[@]}"
do
    echo "Searching for $keyword..."
    awk "/$keyword/" $LOG_FILE | sed "s/$keyword/\e[31m$keyword\e[0m/g"
done
