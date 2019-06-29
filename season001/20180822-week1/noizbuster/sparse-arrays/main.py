#!/bin/python3

import os


def matchingStrings(strings, queries):
    m = dict()  # key, value pair
    o = []      # output buffer

    # accumulate
    for s in strings:
        if s not in m.keys():
            m[s] = 1
        else:
            m[s] += 1
    # write buffer
    for q in queries:
        if q in m.keys():
            o.append(m[q])
        else:
            o.append(0)

    return o


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

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

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
