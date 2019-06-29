#!/bin/python3

import math
import os
import random
import re
import sys

input1 = ['5 3 4', '1 5 8', '6 4 2']
input2 = ['4 9 2', '3 5 7', '8 1 5']
input3 = ['4 8 2', '4 5 7', '6 1 6']

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
  convertedS = convertToIntArr(s)
  
  alternates = [9,8,7,6,5,4,3,2,1]
  # 1. 첫 행이 15가 맞는지 확인한다.
  if sum(convertedS[0]) != 15:
    alternates = set(alternates) - set(convertedS[0])

    for alt in reversed(list(alternates)):
      convertedS[0][0] = alt
      if sum(convertedS[0]) == 15:
        print(alt)
        break
      convertedS[0][1] = alt
      if sum(convertedS[0]) == 15:
        print(alt)
        break
      convertedS[0][2] = alt
      if sum(convertedS[0]) == 15:
        print(alt)
        break
      

  # 2. 15가 아니라면, 같은 행 내에서 중복값이 있는지 확인한다.
  # 3. 중복값이 없다면, 맨 큰 숫자를 15 - (나머지 숫자의 합) = 값으로 바꾼다.

  # 4. 둘째 행이 15가 맞는지 확인한다.
  # 5. 15가 아니라면, 같은 행 또는 1행까지 중복값이 있는지 확인한다.
  # 6. 중복값이 없다면, 맨 큰 숫자를 15 - (나머지 숫자의 합)= 값으로 바꾼다.

  # 7. 셋째 행이 15가 맞는지 확인한다.
  # 8. 15가 아니라면, 같은 행 또는 2행까지 중복값이 있는지 확인한다.
  # 9. 중복값이 

# convert Str array To Int array
def convertToIntArr(s):
  convertedS = []
  for row in s:
    convertedS.append(list(map(lambda x: int(x), row.split(' '))))
  return convertedS

if __name__ == '__main__':
  formingMagicSquare(input1)
