#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(numberList):
  result = []
  
  for n in numberList:
    isFibo = False
    first, second = 1, 1
    if (n < 1):
      pass
    if (n == 1):
      isFibo = True
      pass

    while (n >= second):
      if (n == second):
        isFibo = True
        break
      first, second = second, first + second
    
    r = 'isFibo' if isFibo else 'isNotFibo'
    result.append(r)
    
  return result

if __name__ == '__main__':
    print(solve([5,7,8]))
