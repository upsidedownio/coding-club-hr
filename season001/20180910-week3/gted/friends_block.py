#!/bin/python3


removed_table = {}


def check_window(board, x, y):
    if not board:
        print("Empty board")
    if y < 0 or y+1 >= len(board):
        print("Invalid y index of window")
    if x < 0 or x+1 >= len(board[0]):
        print("Invalid x index of window")
    kfriend_x_y = board[y][x]
    if kfriend_x_y == 'X':
        return
    if board[y+1][x] != kfriend_x_y or \
            board[y][x+1] != kfriend_x_y or \
            board[y+1][x+1] != kfriend_x_y:
        return
    for _x, _y in zip([x, x, x+1, x+1], [y, y+1, y, y+1]):
        if (_x, _y) in removed_table:
            removed_table[(_x, _y)] += 1
        else:
            removed_table[(_x, _y)] = 1


def replace(board, x, y, new_val):
    str_in_list = list(board[y])
    str_in_list[x] = new_val
    board[y] = ''.join(str_in_list)


def clear_removed_slots(board):
    for (x, y), _ in removed_table.items():
        replace(board, x, y, 'X')


def fill_from_upper(board, x, y):
    for _y in range(y-1, -1, -1):
        if board[_y][x] != 'X':
            replace(board, x, y, board[_y][x])
            replace(board, x, _y, 'X')
            break


def rearrange_board(board, m, n):
    for y in range(m-1, -1, -1):
        for x in range(n-1, -1, -1):
            if board[y][x] == 'X':
                fill_from_upper(board, x, y)


def print_board(board, n):
    print("#"*n)
    for row in board:
        print(row)
    print("#"*n + "\n")


def solution(m, n, board):
    answer = 0
    while True:
        for y in range(0, m-1):
            for x in range(0, n-1):
                check_window(board, x, y)
        if not removed_table:
            break
        answer += len(removed_table)
        print("before re-arrange:")
        print_board(board, n)
        clear_removed_slots(board)
        rearrange_board(board, m, n)
        print("after re-arrange:")
        print_board(board, n)
        removed_table.clear()
    return answer

m, n, board = 4, 5,	["CCBDE", "AAADE", "AAABF", "CCBBF"]
# m, n, board = 6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]


if __name__ == '__main__':
    print(solution(m, n, board))
