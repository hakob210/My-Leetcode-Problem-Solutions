#!/bin/bash

sorted_files=$(ls | grep '.py$' | sed -E 's/.*_([0-9]+)\.py/\1 &/' | sort -n | awk '{printf "%s - %s\n", $1, substr($2, index($2,$3))}')

echo "$sorted_files" | awk '{printf "\033[0;31m%d.\033[0m %s\n\n", NR, $0}'

