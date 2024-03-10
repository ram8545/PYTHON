#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    n = len(matrix) // 2
    max_sum = 0

    # Iterate through upper-left quadrant
    for i in range(n):
        for j in range(n):
            # Calculate the sum of corresponding elements in upper-right, lower-left, and lower-right quadrants
            upper_left_sum = matrix[i][j]
            upper_right_sum = matrix[i][2*n-1-j]
            lower_left_sum = matrix[2*n-1-i][j]
            lower_right_sum = matrix[2*n-1-i][2*n-1-j]

            # Update max_sum with the maximum sum of these elements
            max_sum += max(upper_left_sum, upper_right_sum, lower_left_sum, lower_right_sum)

    return max_sum

# Example usage:
# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# print(flippingMatrix(matrix))  # Output: 56

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
