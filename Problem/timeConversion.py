#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hours, minutes, seconds = map(int, s[:-2].split(':'))
    meridian = s[-2:]

    # Convert to 24-hour format
    if meridian == 'AM':
        if hours == 12:
            hours = 0
    else:
        if hours != 12:
            hours += 12

    # Format the result
    return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
