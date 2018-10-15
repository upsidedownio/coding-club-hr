# Complete the surfaceArea function below.
def surfaceArea(A):
    col_count = len(A[0])
    row_count = len(A)

    count = 0
    # 천장, 바닥, 오른쪽 방향, 왼쪽 방향
    for r in range(0, row_count):
        before1 = 0
        before2 = 0
        for c in range(0, col_count): # col = 3, c = [0,1,2]
            # 상, 하
            if A[r][c]  > 0:
                count += 2
            
            # > 오른쪽 (col * h)
            next1 = A[r][c] 
            if before1 < next1:
                count += (next1 - before1)
            before1 = next1

             # <(왼쪽), [0][2], [0][1], [0][0]
            next2 = A[r][col_count -1 -c]
            if before2 < next2:
                count += (next2 - before2)
            before2 = next2

    # 아래 방향, 위 방향
    for c in range(0, col_count):
        before3 = 0
        before4 = 0
        for r in range(0, row_count):
             #  V(아래) , [0][0], [1][0], [2][0]
            next3 = A[r][c]
            if before3 < next3:
                count += (next3 - before3)
            before3 = next3

            # A (위), [2][2], [1][2] [0][2]
            next4 = A[row_count -1 -r][c] 
            if before4 < next4:
                count += (next4 - before4)
            before4 = next4
    return count

if __name__ == "__main__":
    # 60
    H = 3
    W = 3
    A = [[1, 3, 4],
         [2, 2, 3],
         [1, 2, 4]]

    # 34
    # H = 3
    # W = 3
    # A = [[1,2,1],
    #      [1,1,1],
    #      [1,1,1]]

    # 34
    # H = 3
    # W = 3
    # A =  [[0, 1, 0],
    #       [2, 4, 2],
    #       [0, 0, 0]]

    # 28
    # H = 3
    # W = 3
    # A =  [[1, 0, 1],
    #       [1, 0, 1],
    #       [1, 0, 1]]

    # 0
    # H = 3
    # W = 3
    # A =  [[0, 0, 0],
    #       [0, 0, 0],
    #       [0, 0, 0]]

    # 6
    # H = 1
    # W = 1
    # A =  [[1]]


    # 6
    # H = 2
    # W = 3
    # A =  [[0, 0, 0],
    #       [0, 1, 0]]

    print(surfaceArea(A))