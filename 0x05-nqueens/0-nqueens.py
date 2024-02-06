#!/usr/bin/python3
"""
N Queens problem solution
"""

import sys

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at position (row, col)
    """
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True

def solve_queens(board, col, n, solutions):
    """
    Solve N Queens problem using backtracking
    """
    if col == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return
    for row in range(n):
        if is_safe(board, row, col):
            board[col] = row
            solve_queens(board, col + 1, n, solutions)

def print_solutions(solutions):
    """
    Print the solutions
    """
    for solution in solutions:
        print(solution)

def main():
    """
    Main function
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []
    solve_queens(board, 0, n, solutions)
    print_solutions(solutions)

if __name__ == "__main__":
    main()
