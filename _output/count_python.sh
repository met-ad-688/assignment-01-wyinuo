#!/bin/bash

# Count occurrences of "python" (case-insensitive) in both CSV files
count=$(grep -i "python" questions.csv question_tags.csv | wc -l)

# Output the count
echo "Total lines containing 'python': $count"
