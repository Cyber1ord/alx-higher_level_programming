#!/usr/bin/python3

"""
nqueens backtracking program to print the coordinates of n queens
on an N*N grid such that they are all in non-attacking positions
"""


import sys

def solve_nqueens(n):
    solutions = []
    board = [[' ' for _ in range(n)] for _ in range(n)]
    backtrack(board, 0, solutions)
    return solutions

def backtrack(board, row, solutions):
    if row == len(board):
        solutions.append(get_solution(board))
        return
    for col in range(len(board)):
        if is_valid(board, row, col):
            board[row][col] = 'Q'
            backtrack(board, row + 1, solutions)
            board[row][col] = ' '

def is_valid(board, row, col):
    for i in range(row):
        if board[i][col] == 'Q':
            return False
        if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
            return False
        if col + (row - i) < len(board) and board[i][col + (row - i)] == 'Q':
            return False
    return True

def get_solution(board):
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 'Q':
                solution.append([row, col])
                break
    return solution

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = solve_nqueens(n)
    for sol in solutions:
        print(sol)
