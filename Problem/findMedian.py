#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    # Sort the array
    arr.sort()

    # Check if the length of the array is odd or even
    n = len(arr)
    if n % 2 == 0:
        # If even, return the average of the middle two elements
        return (arr[n // 2 - 1] + arr[n // 2]) / 2
    else:
        # If odd, return the middle element
        return arr[n // 2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
