#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

# The left-to-right diagonal = 1 + 5 + 9 = 15. The right to left diagonal = 3 + 5 + 9 = 17 . Their absolute difference is 15 - 17 = 2.

def diagonalDifference(arr):
    # Write your code here
    primary_sum = 0
    secondary_sum = 0

    for i in range(len(arr)):
        primary_sum += arr[i][i]
        secondary_sum += arr[i][len(arr)-1-i]
    absolute_difference = abs(primary_sum - secondary_sum)

    return absolute_difference

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
