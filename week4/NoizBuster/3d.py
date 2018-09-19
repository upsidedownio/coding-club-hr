#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):
    # IV = roof and floor (horizental)
    price = H * W * 2

    # vertical surface
    for i in range(H):
        for j in range(W):
            # border
            price += A[i][j] if i == 0 else 0
            price += A[i][j] if j == 0 else 0
            price += A[i][j] if i == H-1 else 0
            price += A[i][j] if j == W-1 else 0
            # in middle
            price += abs(A[i][j] - A[i][j-1]) if j != 0 else 0
            price += abs(A[i][j] - A[i-1][j]) if i != 0 else 0
    return price

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
