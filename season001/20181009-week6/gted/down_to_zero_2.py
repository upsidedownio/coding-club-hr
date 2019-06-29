#!/bin/python3

import os
import sys


N = 10 ** 6

cost = [-1] * (N+1)
cost[0] = 0
cost[1] = 1
cost[2] = 2
cost[3] = 3


def get_positive_min(a, b):
    if a < 0 and b < 0:
        return 0
    elif a < 0 and b > 0:
        return b
    elif b < 0 and a > 0:
        return a
    else:
        return min(a, b)


for a in range(2, N+1):
    if a - 1 > 3:
        cost[a] = get_positive_min(cost[a], cost[a-1] + 1)
    for b in range(2, a+1):
        if a * b <= N:
            cost[a*b] = get_positive_min(cost[a*b], cost[a] + 1)
        else:
            break


def downToZero(n):
    return cost[n]            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())
        result = downToZero(n)

        fptr.write(str(result) + '\n')

    fptr.close()
