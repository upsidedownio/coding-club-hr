from functools import lru_cache

@lru_cache(maxsize=65536)
def isPower(x):
    return x != 0 and (x & (x - 1)) == 0

def twoTwo(a):
    string = a
    count = 0
    for end_j in range(len(a) -1, -1, -1):
        lastString = string[end_j]
        if lastString == '2' or lastString == '4' or lastString == '6' or lastString == '8':
            totalSubString = ''
            for start_i in range(end_j, -1, -1):
                startString = string[start_i]
                totalSubString = startString + totalSubString
                if startString == '0':
                    continue
                else:
                    if isPower(int(totalSubString)):
                        count += 1
        elif lastString == '1':
            count += 1
    return count

def twoTwo2(a):
    string = a
    count = 0
    for start_i in range(0, len(a)):
        if int(string[start_i]) == 0:
            continue
        beforeSubString = ''
        for end_j in range(start_i, len(a)):
            lastString = string[end_j]
            beforeSubString = beforeSubString + lastString
            # power of 2 => 1, 2, 4, 8, 1(6), 3(2), 6(4), 12(8), 25(6), 51(2)...
            if beforeSubString != '6' and beforeSubString == '1' or lastString == '2' \
               or lastString == '4' or lastString == '6' or lastString == '8':
                if isPower(int(beforeSubString)):
                    count += 1
    # print(isPower.cache_info())
    return count

if __name__ == '__main__':
    print(twoTwo('2222222'))  # 7
    print(twoTwo('24256'))  # 4
    print(twoTwo('65536'))  # 1
    print(twoTwo('023223'))  # 4
    print(twoTwo('33579'))  # 0
    print(twoTwo('666666'))  # 0
   