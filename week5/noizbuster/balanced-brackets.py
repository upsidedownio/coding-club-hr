#!/bin/python3

import math
import os
import random
import re
import sys

def isPair(a, b):
    return {
        '{' : '}',
        '[' : ']',
        '(' : ')'
    }.get(a, None) == b

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    for c in s:
        if len(stack) is 0 or isPair(stack[-1], c) is not True:
            stack.append(c)
        else:
            stack.pop()
    if len(stack) is not 0:
        return 'NO'
    else:
        return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
