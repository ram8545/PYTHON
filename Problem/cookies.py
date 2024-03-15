#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    # Write your code here
    heapq.heapify(A)

    # Initialize the number of operations
    operations = 0

    # While there are at least two cookies and the least sweet cookie is less than the threshold
    while len(A) >= 2 and A[0] < k:
        # Get the two least sweet cookies
        least_sweet = heapq.heappop(A)
        second_least_sweet = heapq.heappop(A)

        # Combine the two cookies and calculate their sweetness
        combined_sweetness = least_sweet + 2 * second_least_sweet

        # Add the combined cookie back to the heap
        heapq.heappush(A, combined_sweetness)

        # Increment the number of operations
        operations += 1

    # Check if all cookies have sweetness greater than or equal to the threshold
    if A[0] < k:
        return -1
    else:
        return operations

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
