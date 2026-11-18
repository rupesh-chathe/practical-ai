"""Practical 8: Human vs AI Tic-Tac-Toe using Minimax."""

import math

board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board(b):
    print('\n')
    for i in range(3):
        print(f' {b[i][0]} | {b[i][1]} | {b[i][2]} ')
        if i < 2:
            print('---|---|---')
    print('\n')

def check_winner(b):
    """Return 10 for X win, -10 for O win, 0 otherwise."""
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != ' ':
            return 10 if b[i][0] == 'X' else -10
        if b[0][i] == b[1][i] == b[2][i] != ' ':
            return 10 if b[0][i] == 'X' else -10
    if b[0][0] == b[1][1] == b[2][2] != ' ':
        return 10 if b[0][0] == 'X' else -10
    if b[0][2] == b[1][1] == b[2][0] != ' ':
        return 10 if b[0][2] == 'X' else -10
    return 0

def is_moves_left(b):
    return any(' ' in row for row in b)

def minimax(b, depth, is_max):
    score = check_winner(b)
    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not is_moves_left(b):
        return 0

    if is_max:
        best = -math.inf
        for r in range(3):
            for c in range(3):
                if b[r][c] == ' ':
                    b[r][c] = 'X'
                    best = max(best, minimax(b, depth + 1, False))
                    b[r][c] = ' '
        return best

    best = math.inf
    for r in range(3):
        for c in range(3):
            if b[r][c] == ' ':
                b[r][c] = 'O'
                best = min(best, minimax(b, depth + 1, True))
                b[r][c] = ' '
    return best

def find_best_move(b):
    best_val = -math.inf
    best_move = (-1, -1)
    for r in range(3):
        for c in range(3):
            if b[r][c] == ' ':
                b[r][c] = 'X'
                move_val = minimax(b, 0, False)
                b[r][c] = ' '
                if move_val > best_val:
                    best_val = move_val
                    best_move = (r, c)
    return best_move

def play_game():
    print("--- Tic-Tac-Toe: Human ('O') vs Agent ('X') ---")
    print('Enter grid positions as row and column numbers (0, 1, or 2).')
    print_board(board)

    while is_moves_left(board) and check_winner(board) == 0:
        while True:
            try:
                row = int(input('Enter Row (0-2): '))
                col = int(input('Enter Column (0-2): '))
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                    board[row][col] = 'O'
                    break
                print('Invalid move. Cell is either occupied or out of bounds.')
            except ValueError:
                print('Invalid input. Please enter numbers between 0 and 2.')
        print_board(board)

        if check_winner(board) != 0 or not is_moves_left(board):
            break

        print("Agent ('X') is thinking...")
        r, c = find_best_move(board)
        board[r][c] = 'X'
        print(f'Agent chose cell: ({r}, {c})')
        print_board(board)

    score = check_winner(board)
    if score == 10:
        print("Game Over: Agent ('X') Wins!")
    elif score == -10:
        print("Game Over: You ('O') Win!")
    else:
        print("Game Over: It's a Draw!")

if __name__ == '__main__':
    play_game()
