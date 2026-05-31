#!/usr/bin/python3
import sys

# Start the range from 1 instead of 0 to skip the script name
for i in range(1, len(sys.argv)):
    print(sys.argv[i])