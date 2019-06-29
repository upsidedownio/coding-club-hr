#!/bin/python3

import os
import sys


def get_num_len(x):
    count = 0
    while (x > 0.999):
        x = x / 10
        count = count + 1
    return count


# Setup
pow2nums = []
for i in range(0, 801):
    pow2num = 2 ** i
    pow2num_len = get_num_len(pow2num)
    pow2nums.append(str(pow2num))
max_len = len(pow2nums[-1])


def how_many_times_substring_found(string, sub_string):
    count = 0
    start_i = 0
    while True:
        start_i = string.find(sub_string, start_i)
        if start_i > -1:
            count += 1
            start_i += len(sub_string)
            # start_i += 1
        else:
            break
    return count


def twoTwo(x):
    count = 0
    for pow2num in pow2nums:
        count += how_many_times_substring_found(x, pow2num)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        x = input()
        result = twoTwo(x)
        fptr.write(str(result) + '\n')
    fptr.close()
