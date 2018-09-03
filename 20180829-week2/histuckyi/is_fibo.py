from functools import lru_cache
"""
 hackerrank : Is Fibo
 https://www.hackerrank.com/challenges/is-fibo/problem

time limit : 10
Memory limit : 512

> input
3
5
7
8

> output
IsFibo
IsNotFibo
IsFibo
"""
from functools import lru_cache

@lru_cache(maxsize=512)
def fibo(n):
    if n < 2:
        return n
    return fibo(n-1) + fibo(n-2)


def solve1(n):
    result = 0
    cnt = 0
    while result < n:
        result = fibo(cnt)
        if result == n:
            return 'IsFibo'
        cnt += 1
    return 'IsNotFibo'


def solve2(n):
    result = 0
    first = 1
    second = 1
    if n < 2:
        return "IsFibo"
    while result < n:
        result = first + second
        if result == n:
            return "IsFibo"
        first = second
        second = result
    return 'IsNotFibo'

if __name__ == "__main__":
    t = int(input())

    for t_itr in range(t):
        n = int(input())
        result = solve1(n)
        # result = solve2(n)
        print(result)
