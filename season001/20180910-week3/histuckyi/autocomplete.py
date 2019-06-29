

"""
 hackerrank : autocomplete
 https://programmers.co.kr/learn/courses/30/lessons/17685
"""
def solution(words):
    word_cnt = 0 # total word count
    words.sort() # sorting

    for word_idx in range(len(words)):
        current_word = words[word_idx] #  word to look for
        current_word_length = len(current_word)
        current_word_last_index = current_word_length -1  # length -> last index
        front_idx = -1 # Index matching with previous word
        back_idx = -1 # Index matching with back word

        # idx == 0 -> pass
        if word_idx > 0:
            front_word = words[word_idx -1]
            for i in range(current_word_length):
                if i == len(front_word):
                    break
                if front_word[i] == current_word[i]:
                    front_idx += 1
                else:
                    break

        # idx == last index -> pass
        if word_idx < len(words) - 1:
            back_word = words[word_idx +1]
            for j in range(current_word_length):
                if j == len(back_word):
                    break
                if back_word[j] == current_word[j]:
                    back_idx += 1
                else:
                    break

        # both front,back word do not match the current word -> 1 character
        if front_idx == -1 and back_idx == -1:
            word_cnt += 1
        else:
            max_idx = max(front_idx, back_idx)
            max_cnt = max_idx + 1 # idex -> length
            # @warning, if more than word length, one more character. (index + 1) + 1 
            if max_idx < current_word_last_index:
                max_cnt += 1
            word_cnt += max_cnt  
    return word_cnt

if __name__=="__main__":
    print(solution(['go','gone','guild']))  # result : 7
    print(solution(['abc','def','ghi','jklm'])) # result : 4
    print(solution(['word','war','warrior','world'])) # result : 15
                