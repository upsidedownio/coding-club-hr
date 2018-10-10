#!/bin/python3

import os
import sys
import math

cache = dict()
cache[0] = -1
cache[1] = 1
cache[2] = 2

def aliquots(N):
    output = []
    IV = math.ceil(math.sqrt(N))
    for i in range(2, IV):
        if N % i is 0:
            output.append(max(i, N//i))
    output = list(set(output))
    output.append(N-1)
    output.sort()
    print('aliquots of', N, output)
    return output

def findShortCut(N):
    # i = int(math.sqrt(n))
    # while i >= 2:
    #     if n % i == 0:
    #         return max(i, n // i)
    #     else:
    #         i -= 1
    #
    # return 0
    if N in cache:
        # print('cache[', N, '] is', cache[N])
        return cache[N]
    # IV = math.ceil(math.sqrt(N))
    # for i in range(IV, 1, -1):
    #     if N % i is 0:
    #         cache[N] = max(i, N // i)
    #         return max(i, N // i)
    # cache[N] = N
    # return N
    children = aliquots(N)
    optimal = N
    next = N
    if len(children) is 0:
        step = findShortCut(N-1) + 1
        # print('cache[', N, '] is', step)
        cache[N] = step
        return step

    for child in children:
        step = findShortCut(child) + 1
        if step < optimal:
            optimal = min(step, optimal)
            next = child
    cache[N] = optimal
    print('cache[', N, '] is', optimal, 'from[', next, ']', cache[next])
    return optimal


#
# Complete the downToZero function below.
#
def downToZero(n):
    output = findShortCut(n)
    return output
    # cursor = n
    # step = 0
    # history = ''
    # while cursor > 0 :
    #     next = findShortCut(cursor)['next']
    #     if cursor == next:
    #         cursor -= 1
    #     else:
    #         cursor = next
    #     step += 1
    #     history += ' => ' + str(cursor)
    #
    # print('from', n, history)
    # return step



    # moves = [n]
    # q = []
    # q.append(n)
    #
    # while len(q) > 0:
    #     current = q.pop()
    #     if current == 0:
    #         return len(moves) - 1
    #
    #     factor = findShortCut(current)
    #
    #     if factor == current:
    #         moves.append(current - 1)
    #         q.append(current - 1)
    #     else:
    #         moves.append(factor)
    #         q.append(factor)

    #
    # Write your code here.
    #

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = downToZero(n)

        print(str(result))
        # fptr.write(str(result) + '\n')

    # fptr.close()
