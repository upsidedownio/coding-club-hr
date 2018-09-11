"""
 hackerrank : friends 4 block
 https://programmers.co.kr/learn/courses/30/lessons/17679
"""
dx = [0, 1, 1] # row
dy = [1, 1, 0] # col
brocken_blocks_count = 0 # number of broken blocks

# recursion
def game(n, m , board):
    global brocken_blocks_count
    block_set = set()

    # 1
    # traverse all elements of matirx
    # check if tree directions(ight, diagonal below, and below) have same character.
    for index_x in range(0, n-1):
        for index_y in range(0, m-1):
            value = board[index_x][index_y]
            if value == 0:
                continue

            check_cnt = 0
            block_list = []
            for i in range(3):
                ad_x = index_x + dx[i]
                ad_y = index_y + dy[i]
                # out of range -> pass
                if ad_x < 0 or ad_y < 0 or ad_x >=n or ad_y >=m:
                    break
                # not match -> pass
                if board[ad_x][ad_y] != value:
                    break

                check_cnt += 1 # checking count + 1
                block_list.append((ad_x, ad_y))
                # 2
                # if check all three direction, all element append to the block list
                if check_cnt == 3:
                # | : union operator
                # test1 = {1,2,3}
                # test2 = [3,4,5]
                # test1 |= set(test2)
                # test1 # {1,2,3,4,5}
                    block_list.append((index_x, index_y))
                    block_set |= set(block_list)  # union to the block list 

    # if block_set is enmpty, exit the recursion function.
    if len(block_set) == 0:
        return brocken_blocks_count
    else:
        # 3
        # record 
        while block_set:
            brocken_blocks_count += 1
            breaked_point = block_set.pop()
            board[int(breaked_point[0])][int(breaked_point[1])] = 0

        # 4 
        # pull down blocks
        for col in range(0, m):
            for row in range(n-1, -1, -1):
                if board[row][col] == 0:
                    not_zero_x = row - 1
                    # move until next is not 0
                    while not_zero_x > -1:
                        if board[not_zero_x][col] != 0:
                            break
                        else:
                            not_zero_x -= 1

                    # all is 0
                    if not_zero_x == -1:
                        break
                    
                    # exchange values with each other
                    board[row][col] , board[not_zero_x][col] = board[not_zero_x][col], board[row][col]

                    # last row(0) is not zero, do not need to check anymore.
                    #  go to next turn.
                    if not_zero_x == 0:
                        break
        return game(n, m, board)

def solution(n,m,_board):
    global brocken_blocks_count
    board = []
    for line in _board:
        board.append(list(line))
    result = game(n,m,board) # 함수 시작
    brocken_blocks_count = 0
    return result


if __name__=="__main__":
    # result : 18
    print(solution(4, 5, ['AAAAA','AABAA','AAAAA','AAAAA']))        
    
    # result : 24
    print(solution(5, 6, ["AAAAAA", "BBAATB", "BBAATB", "JJJTAA", "JJJTAA"]))

    # result : 75
    print(solution(5, 15, ["AAAAAAAAAAAAAAA", "AAAAAAAAAAAAAAA", "AAAAAAAAAAAAAAA", "AAAAAAAAAAAAAAA", "AAAAAAAAAAAAAAA"]))
    
    # result : 0
    print(solution(2, 2, ['at','tt']))

    # result : 14
    print(solution(4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']))

    # result : 16
    print(solution(7, 6, ['AJTMFT','TTNNNT','MMNNJJ','RRFACC','RRRFCC','CBNNTJ', 'ATNNJJ']))

    # result : 14
    print(solution(4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']))

    # result : 15
    print(solution(6, 6, ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']))