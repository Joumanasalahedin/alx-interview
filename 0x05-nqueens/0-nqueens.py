#!/usr/bin/python3

import sys


def print_solution(solution):
    print([[i, solution[i]] for i in range(len(solution))])


def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N, row, board):
    if row == N:
        print_solution(board)
    else:
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                solve_nqueens(N, row + 1, board)
                board[row] = -1


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1 for _ in range(N)]
    solve_nqueens(N, 0, board)


if __name__ == "__main__":
    main()