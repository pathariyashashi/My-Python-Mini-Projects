# Tic Tac Toe Game

board = [" " for i in range(9)]

# Board print function
def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

# Winner check function
def check_winner(player):

    # Rows
    if board[0] == board[1] == board[2] == player:
        return True
    if board[3] == board[4] == board[5] == player:
        return True
    if board[6] == board[7] == board[8] == player:
        return True

    # Columns
    if board[0] == board[3] == board[6] == player:
        return True
    if board[1] == board[4] == board[7] == player:
        return True
    if board[2] == board[5] == board[8] == player:
        return True

    # Diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True

    return False

# Main Game
current_player = "X"

for turn in range(9):

    print_board()

    move = int(input(f"Player {current_player}, enter position (1-9): ")) - 1

    # Check empty place
    if board[move] == " ":
        board[move] = current_player
    else:
        print("Position already taken!")
        continue

    # Winner check
    if check_winner(current_player):
        print_board()
        print(f"Player {current_player} Wins!")
        break

    # Player change
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

else:
    print_board()
    print("Match Draw!")