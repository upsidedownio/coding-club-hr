#!/bin/python3

import math
import os
import random
import re
import sys


lbs = ['[', '{', '(']


def matched(lb, rb):
    if lb == '[' and rb == ']':
        return True
    elif lb == '{' and rb == '}':
        return True
    elif lb == '(' and rb == ')':
        return True
    else:
        return False


# Complete the isBalanced function below.
def isBalanced(s):
    lb_stack = []
    for br in s:
        if br in lbs:
            lb_stack.insert(0, br)
        else:
            try:
                lb = lb_stack.pop(0)
                if not matched(lb, br):
                    return "NO"
            except IndexError:
                return "NO"
    if lb_stack:
        return "NO"
    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
