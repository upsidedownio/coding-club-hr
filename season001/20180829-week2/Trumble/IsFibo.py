#!/bin/python3

import os
import sys

scale = 10 ** 10

def get_fibo(n):
    fibo = [0,1]
    i = 1
    while fibo[i] <= scale:
        i += 1
        fibo.append(0)
        fibo[i] = fibo[i-1] + fibo[i-2]
        if fibo[i] == n:
            return "IsFibo"
        elif fibo[i] > n:
            return "IsNotFibo"
    return "IsNotFibo"

def solve(n):
    if n == 0:
        return "IsFibo"
    elif n == 1:
        return "IsFibo"

    return(get_fibo(n))
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()
