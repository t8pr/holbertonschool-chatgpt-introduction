#!/usr/bin/python3

def print_board(board):
    """Prints the current state of the game board."""
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:  # Clean presentation logic without an extra trailing line
            print("-" * 9)

def check_winner(board):
    """Checks the rows, columns, and diagonals for a winning match."""
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    """Checks if there are no more empty spaces left on the board (Tie state)."""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        
        # Robust user input handling
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            
            # Boundary check
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Invalid range! Coordinates must be 0, 1, or 2. Try again.")
                print("-" * 20)
                continue
        except ValueError:
            print("Invalid input! Please enter numbers only (0, 1, or 2).")
            print("-" * 20)
            continue

        # Spot availability check
        if board[row][col] == " ":
            board[row][col] = player
            
            # Check for a winner IMMEDIATELY before switching players
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break
                
            # Check for a draw state
            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            
            # Toggle current player switch
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")
            print("-" * 20)

if __name__ == "__main__":
    tic_tac_toe()
