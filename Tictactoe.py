
#Variables
turn = 0
p_move = 0
p_choice = False
p_newgame = False
game_status =True
game_run = True
game_win = False
game_tie = False
game_board = ["-", "-", "-","-", "-", "-","-", "-", "-"]
current_player = "X"


def show_board():
    print("-" * 50)
    print(f"{game_board[0]}  |  {game_board[1]}  |  {game_board[2]}")
    print(f"{game_board[3]}  |  {game_board[4]}  |  {game_board[5]}")
    print(f"{game_board[6]}  |  {game_board[7]}  |  {game_board[8]}")


#--------------------------Functions------------------------

#Check game conditions Fuctions
def win():
    horizontal_win()
    vertical_win()
    diag_win()


def horizontal_win():
    global game_run
    global game_win
    if game_board[0] == game_board[1] == game_board[2] == "X" or game_board[0] == game_board[1] == game_board[2] == "O":
        game_run = False
        game_win = True
    if game_board[3] == game_board[4] == game_board[5] == "X" or game_board[3] == game_board[4] == game_board[5] == "O":
        game_run = False
        game_win = True
    if game_board[6] == game_board[7] == game_board[8] == "X" or game_board[6] == game_board[7] == game_board[8] == "O":
        game_run = False
        game_win = True


def vertical_win():
    global game_run
    global game_win
    if game_board[0] == game_board[3] == game_board[6] == "X" or game_board[0] == game_board[3] == game_board[6] == "O":
        game_run = False
        game_win = True
    if game_board[1] == game_board[4] == game_board[7] == "X" or game_board[1] == game_board[4] == game_board[7] == "O":
        game_run = False
        game_win = True
    if game_board[2] == game_board[5] == game_board[8] == "X" or game_board[2] == game_board[5] == game_board[8] == "O":
        game_run = False
        game_win = True


def diag_win():
    global game_run
    global game_win
    if game_board[0] == game_board[4] == game_board[8] == "X" or game_board[0] == game_board[4] == game_board[8] == "O":
        game_run = False
        game_win = True
    if game_board[2] == game_board[4] == game_board[6] == "X" or game_board[2] == game_board[4] == game_board[6] == "O":
        game_run = False
        game_win = True


def tie():
    global game_run
    global game_tie
    if turn == 9:
        game_run = False
        game_tie = True


#Player Functions
def player_input():
    global p_move
    print(f"{current_player} Turn")
    p_move = int(input("Your move: "))


def player_swap(player):
    global current_player
    if player == "X":
        current_player = "O"
    else:
        current_player = "X"


def player_check():
    global p_move
    while p_move < 1 or p_move > 9:
        print("Move has to be between 1-9")
        p_move = int(input("Your move : "))
    while game_board[p_move-1] != "-":
        print("Tile already been chosen")
        p_move = int(input("Your move: "))


def player_newgame():
    global turn
    global p_choice
    global game_run
    global game_status
    global game_win
    global game_tie
    global game_board
    p_choice = input("Do you want to start a new game? (y/n): ")
    if p_choice == "y":
        turn = 0
        game_run = True
        game_win = False
        game_tie = False
        game_board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    else:
        game_status = False


#Game Functions
def change_board():
    global turn
    game_board[p_move - 1] = current_player
    turn +=1


def main():
    show_board()
    player_input()
    player_check()
    change_board()
    tie()
    win()


def run():
    while game_run == True:
        main()
        if game_run == True:
             player_swap(current_player)
    if game_win == True:
        show_board()
        print(f"Game result: {current_player} win")
    if game_tie == True:
        show_board()
        print("Game result: Tie")
    player_newgame()


#--------------------------Game------------------------

while game_status == True:
    run()