def solution(words):
    answer = 0
    true_cnt = 0
    answer_list = []
    flag = True

    for i in range(len(words)): 
        check = words.pop(0)
        answer_list = [0] * len(words)
        for j in range(len(check)):
            for k in range(len(words)):
                if check[:j+1] != words[k][:j+1]:
                    true_cnt += 1
                    if true_cnt >= len(words): 
                        answer += 1
                        flag = False
                else:
                    answer += 1
                    break
            true_cnt = 0
            if flag == False:
                flag = True
                break
        words.append(check)
    return answer

print(solution(["go", "gone", "guild"]))