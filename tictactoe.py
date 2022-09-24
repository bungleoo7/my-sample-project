def main():
    player = next_player("")
    board = create_board()
    while not (winner(board) or draw(board)):
        display_board(board)
        players_move(player, board)
        player = next_player(player)
    display_board(board)
    print("Good game. Thanks for playing!") 


# we'll start off with creating the board first.
def create_board():
    board = [] #these will act as the squares
    for square in range(9): #this is how we'll choose our place on the board
        board.append(square) #keeps adding a square (specifically at the end)
    return board


# next, the board must be displayed
def display_board(board): #uses board as the variable since thats what we are displaying
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 

def players_move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): ")) # this is how the player will choose his spot
    board[square - 1] = player 

def next_player(currentplayer):
    if currentplayer == "" or currentplayer == "o":
        return "x"
    elif currentplayer == "x":
        return "o"


if __name__ == "__main__":
    main()
