def twoTwo(a):
    ref = makeRef(a)
    count_list = []
    for n in a[1:]:
        count_list.append(findStrength(n, ref))

    return count_list

def makeRef(a):
    maxN = max(a)
    ref = []
    n = 1
    while(n <= maxN):
        n *= 2
        ref.append(n)

    return ref

def findStrength(n, ref):
    str_n = str(n)
    count = 0

    for n in ref:
        count += str_n.count(str(n))

    return count


if __name__ == '__main__':
    test = [5, 2222222, 24256, 65536, 23223, 33579]
    print(twoTwo(test))