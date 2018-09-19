#!/bin/python3

import math
import os
import random
import re
import sys

neighbor_distances = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# Complete the surfaceArea function below.
def surfaceArea(A, h, w):
    cost = 0
    for i in range(0, h):
        for j in range(0, w):
            basic_cost = 2 + A[i][j] * 4
            cost_deduction = 0
            for distance in neighbor_distances:
                i_prime = i + distance[0]
                j_prime = j + distance[1]
                if i_prime >= 0 and i_prime < h and \
                        j_prime >= 0 and j_prime < w:
                    deduction = A[i_prime][j_prime] if A[i_prime][j_prime] < A[i][j] else A[i][j]
                    cost_deduction += deduction
            cost += (basic_cost - cost_deduction)
    return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    HW = input().split()
    H = int(HW[0])
    W = int(HW[1])
    A = []
    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))
    result = surfaceArea(A, H, W)
    fptr.write(str(result) + '\n')
    fptr.close()
