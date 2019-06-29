import copy
import os
from time import sleep

def find_friends(m,n):
    for i in range(m-1):
        for j in range(n-1):
            if friends[i][j] != None:
                if friends[i][j] == friends[i+1][j] and friends[i][j] == friends[i][j+1] and friends[i][j] == friends[i+1][j+1]:
                    pop_flag[i][j] = 1
                    pop_flag[i+1][j] = 1
                    pop_flag[i][j+1] = 1
                    pop_flag[i+1][j+1] = 1

def pop_friends(m,n):
    global pop_count
    for i in range(m):
        for j in range(n):
            if pop_flag[i][j] == 1:
                pop_count += 1
                friends[i][j] = None

def change_friends(m,n):#to_change
    global cnt
    cnt += 1
    for i in reversed(range(m)):
        for j in range(n):
            if friends[i][j] == None:
                for k in reversed(range(i)):
                    if friends[k][j] != None:
                        friends[i][j] = friends[k][j]
                        friends[k][j] = None
                        break
            os.system('clear')
            """print(cnt)
            for q in range(len(friends)):
                print(friends[q])
            sleep(0.5)"""
            

def friending(m,n):
    find_friends(m,n)
    pop_friends(m,n)
    change_friends(m,n)

def solution(m, n, board):
    global friends, pop_flag, pop_count, cnt
    cnt = 0
    friends = []
    pop_flag = []
    pop_count = 0
    pop_flag = []
    answer = 0

    for i, freind in enumerate(board):
        pop_flag.append([])
        friends.append(list(freind))
        pop_flag[i] = [0 for j in freind]
    stop_flag = copy.deepcopy(pop_flag)
    friending(m,n)
    answer += pop_count
    pop_count = 0

    while pop_flag != stop_flag:
        for i in range(m):
            pop_flag[i] = [0 for j in range(n)]
        friending(m,n)
        answer += pop_count
        pop_count = 0
    
    return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))