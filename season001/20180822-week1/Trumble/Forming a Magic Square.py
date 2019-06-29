from itertools import *

cost = 0
num_list = list()
all_list = list()
cost_list = list()

for i in range(3):
    num_list.extend(list(map(int, input().split(' '))))

#make all list of possible
for all in permutations(range(1,10)):
    if sum(all[0:3]) == 15 and sum(all[3:6]) == 15 and sum(all[6:9]) == 15:
        if sum([all[0],all[3],all[6]]) == 15 and sum([all[1],all[4],all[7]]) == 15 and sum([all[2],all[5],all[8]]) == 15:
            if sum([all[0],all[4],all[8]]) == 15 and sum([all[2],all[4],all[6]]) == 15:
                all_list.append(all)

for i in range(len(all_list)):
    for j in range(len(all_list[i])):
        if num_list[j] != all_list[i][j]:
            cost += abs(num_list[j] - all_list[i][j])
    cost_list.append(cost)
    cost = 0
print(min(cost_list))
