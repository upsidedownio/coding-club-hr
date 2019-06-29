import math
import os
import random
import re
import sys

"""
 hackerrank : Sparse Arrays
 https://www.hackerrank.com/challenges/sparse-arrays/problem
"""
# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    # extract keys without duplication
    key_list = set(strings) 
    # create dict using elements in keyList
    key_dict = dict.fromkeys(key_list, 0) 
    for char in strings:
            key_dict[char] += 1
    for query in queries:
        result = 0
        if query in key_list:
            result = key_dict[query]
        yield result

if __name__ == '__main__':
    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)
    print('\n'.join(map(str, res)))

    
