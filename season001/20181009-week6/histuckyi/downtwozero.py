import math

class Node(object):
    def __init__(self, data, count):
        self.data = data
        self.count = count

def case1(node, queue, countList):
    current_count = node.count
    next_count = current_count + 1
    current_data = node.data

    try:
        if next_count < countList[str(current_data - 1)]:
            queue.append(Node(current_data - 1, current_count+ 1))
            countList[str(current_data - 1)] = next_count
    except KeyError as error:
        queue.append(Node(current_data - 1, next_count))
        countList[str(current_data - 1)] = next_count


def case2(node, queue, countList):
    current_data = node.data
    current_count = node.count
    next_count = current_count + 1
    maxCut = int(math.sqrt(current_data))

    for cut in range(2, maxCut + 1):
        if current_data % cut == 0:
            answer = current_data // cut
            try:
                if next_count < countList[str(answer)]:
                    queue.append(Node(answer, next_count))
                    countList[str(answer)] = next_count
            except KeyError as error:
                queue.append(Node(answer, next_count))
                countList[str(answer)] = next_count

def downToZero(n):
    queue = []
    countList = {}
    num = n
    queue.append(Node(num, 0))
    
    countList['0'] = 1000000

    if num == 0:
        return 0
    
    while queue:
        node = queue.pop(0)
        current_data = node.data
        current_count = node.count
        next_count = current_count + 1

        if next_count >= countList['0']:
            continue
        
        # case1 : decrease value by 1
        if current_data >= 1:
            case1(node, queue, countList)

        # case2 : a x b (a != 1, b !=1), N = max(a, b)
        if current_data >= 4:
            case2(node, queue, countList)
    
    print(countList['0'])
    return countList['0']


if __name__ == "__main__":
    downToZero(1) # 1->0 : 1
    downToZero(2) # 2->1->0 : 2
    downToZero(3)  # 3->2->1->0 : 3
    downToZero(4)  # 4->2->1->0 : 3
    downToZero(5)  # 5->4->2->1->0 : 4
    downToZero(6)  # 6->3->2->1->0 : 4
    downToZero(7) # 7->6->3->2->1->0 : 5
    print('\n')

    downToZero(12)  # 12->4->2->1->0 : 4
    downToZero(16) # 16->4->2->1->0 : 4
    downToZero(33) # 33->32->8->4->2->1->0 : 6
    downToZero(34) # 34->17->16->4->2->1->0 : 6
    downToZero(86) # 86->85->84->12->4->2->1->0 : 7
    downToZero(125)  # 125->25->5->4->2->1->0 : 6
    print('\n')

    downToZero(168) # 168->84->12->4->2->1->0 : 6
    downToZero(256) # 256->16->4->2->1->0 : 5
    downToZero(257) # 257->256->16->4->2->1->0 : 6
    downToZero(1000)  # 1000->40->8->4->2->1->0 : 6
    downToZero(2436)  # 2436->84->12->4->2->1->0 : 6
    print('\n')

    downToZero(11565) # 11565->257->256->16->4->2->1->0 : 7
    downToZero(11566) # 11566->11565->257->256->16->4->2->1->0 : 8
    downToZero(46264) # 46264->46263->6609->6608->112->16->4->2->1->0 : 9
    downToZero(214567)  # 214567->9329->9328->176->16->4->2->1->0 : 8
    downToZero(225604)  # 225604->56401->56400->240->16->4->2->1->0 : 8
    print('\n')

    downToZero(603900)  # 603900->9900->132->12->4->2->1->0 : 7
    downToZero(808707)  # 808707->1717->1716->132->12->4->2->1->0 : 8
    downToZero(812849)  # 812849->812848->1616->1615->85->84->12->4->2->1->0 : 10
    downToZero(833352)  # 833352->5342->5341->109->108->12->4->2->1->0 : 9
    downToZero(999999)  # 999999->2457->63->9->3->2->1->0 : 7
    downToZero(1000000)  # 1000000->20000->160->16->4->2->1->0 : 7
    print('\n')
    