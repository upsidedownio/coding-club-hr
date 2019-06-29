#!/bin/python3

import math
import os
import random
import re
import sys

magic_squares = []
magic_squares.append([[8, 3, 4], [1, 5, 9], [6, 7, 2]])
magic_squares.append([[6, 7, 2], [1, 5, 9], [8, 3, 4]])
magic_squares.append([[4, 9, 2], [3, 5, 7], [8, 1, 6]])
magic_squares.append([[2, 9, 4], [7, 5, 3], [6, 1, 8]])
magic_squares.append([[2, 7, 6], [9, 5, 1], [4, 3, 8]])
magic_squares.append([[4, 3, 8], [9, 5, 1], [2, 7, 6]])
magic_squares.append([[6, 1, 8], [7, 5, 3], [2, 9, 4]])
magic_squares.append([[8, 1, 6], [3, 5, 7], [4, 9, 2]])


# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    min_diff_sum = 45
    for ms in magic_squares:
        diff_sum = 0
        for s_row, ms_row in zip(s, ms):
            diff_sum += sum(list(map(lambda x: abs(x[0] - x[1]), zip(s_row, ms_row))))
        if diff_sum < min_diff_sum:
            min_diff_sum = diff_sum
    return min_diff_sum

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
