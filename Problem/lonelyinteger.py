#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Count occurrences of each element in the list
    counts = Counter(a)
    # counts output = ({1: 2, 2: 2, 3: 2, 4: 1})
    # Iterate through the counts and return the element with a count of 1
    for element, count in counts.items():
        if count == 1:
            return element


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
