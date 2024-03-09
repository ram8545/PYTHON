
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive = 0
    negative = 0
    zeros = 0
    for i in arr:
        if int(i) > 0:
            positive += 1
        elif int(i) < 0:
            negative += 1
        else:
            zeros += 1
    print(positive / len(arr))
    print(negative / len(arr))
    print(zeros / len(arr))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)


# n = 6
# arr = [-4, 3, -9, 0, 4, 1]
# positive = 0.500000
# negative = 0.333333
# zeros = 0.166667
