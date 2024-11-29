import random
import os

# Initialize the game board
def initialize_board():
    board = [[0] * 4 for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

# Add a new tile to the board
def add_new_tile(board):
    empty_cells = [(r, c) for r in range(4) for c in range(4) if board[r][c] == 0]
    if empty_cells:
        r, c = random.choice(empty_cells)
        board[r][c] = 2 if random.random() < 0.9 else 4

# Print the board
def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in board:
        print("+----" * 4 + "+")
        print("|" + "|".join(f"{num:^4}" if num else "    " for num in row) + "|")
    print("+----" * 4 + "+")

# Merge a row or column to the left
def merge_left(row):
    non_zero = [num for num in row if num != 0]
    merged = []
    skip = False
    for i in range(len(non_zero)):
        if skip:
            skip = False
            continue
        if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
            merged.append(non_zero[i] * 2)
            skip = True
        else:
            merged.append(non_zero[i])
    return merged + [0] * (4 - len(merged))

# Transpose the board (for up and down moves)
def transpose(board):
    return [list(row) for row in zip(*board)]

# Reverse the board (for right and down moves)
def reverse(board):
    return [row[::-1] for row in board]

# Move tiles on the board
def move(board, direction):
    if direction in ['w', 's']:
        board = transpose(board)
    if direction in ['d', 's']:
        board = reverse(board)

    new_board = [merge_left(row) for row in board]

    if direction in ['d', 's']:
        new_board = reverse(new_board)
    if direction in ['w', 's']:
        new_board = transpose(new_board)
    
    return new_board

# Check if moves are possible
def is_game_over(board):
    for r in range(4):
        for c in range(4):
            if board[r][c] == 0:
                return False
            if r < 3 and board[r][c] == board[r + 1][c]:
                return False
            if c < 3 and board[r][c] == board[r][c + 1]:
                return False
    return True

# Main game loop
def main():
    board = initialize_board()
    while True:
        print_board(board)
        if is_game_over(board):
            print("Game Over!")
            break
        move_dir = input("Enter move (w=up, s=down, a=left, d=right): ").strip().lower()
        if move_dir not in ['w', 'a', 's', 'd']:
            print("Invalid move. Use w, a, s, or d.")
            continue
        
        new_board = move(board, move_dir)
        if new_board != board:
            board = new_board
            add_new_tile(board)

if __name__ == "__main__":
    main()
