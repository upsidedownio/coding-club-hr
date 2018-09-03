#!/bin/python3

import os
import sys

fibo_nums = {}
fibo_nums[0] = 0
fibo_nums[1] = 1


# Complete the solve function below.
def solve(n):
    k = 2
    k_th_fibo = get_fibo(k)
    while k_th_fibo < n:
        k += 1
        k_th_fibo = get_fibo(k)
    if k_th_fibo == n:
        return "IsFibo"
    else:
        return "IsNotFibo"


# set limitation of size of memoization
def get_fibo(k):
    if k in fibo_nums:
        pass
    else:
        fibo_nums[k] = get_fibo(k-1) + get_fibo(k-2)
    return fibo_nums[k]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)
        fptr.write(result + '\n')

    fptr.close()
