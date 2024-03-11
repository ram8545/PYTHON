#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def is_palindrome(s):
    return s == s[::-1]

def palindromeIndex(s):
    # Write your code here
    if is_palindrome(s):
        return -1

    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            if is_palindrome(s[:i] + s[i + 1:]):
                return i
            elif is_palindrome(s[:n - 1 - i] + s[n - i:]):
                return n - 1 - i

    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
