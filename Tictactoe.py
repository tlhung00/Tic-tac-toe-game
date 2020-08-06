#Board
game_board = ["-", "-", "-",
              "-", "-", "-",
              "-", "-", "-"]
#Variables
turn = 0
p_choice = 0
game_run = True
game_win = False
game_tie = False
current_player = "X"


def show_board():
    print(f"{game_board[0]}  |  {game_board[1]}  |  {game_board[2]}")
    print(f"{game_board[3]}  |  {game_board[4]}  |  {game_board[5]}")
    print(f"{game_board[6]}  |  {game_board[7]}  |  {game_board[8]}")

#Win and tie
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


#player
def player_input():
    global p_choice
    print(f"{current_player} Turn")
    p_choice = int(input("Your move: "))

def player_swap(player):
    global current_player
    if player == "X":
        current_player = "O"
    else:
        current_player = "X"

#logic
def change_board():
    global turn
    game_board[p_choice - 1] = current_player
    turn +=1

def game():
    show_board()
    player_input()
    player_input_check()
    change_board()
    win()
    tie()

def player_input_check():
    global p_choice
    while p_choice < 1 or p_choice > 9:
        print("Move is not allowed")
        p_choice = int(input("Your move: "))


#game
while game_run == True:
    game()
    if game_run == True:
         player_swap(current_player)
if game_win == True:
    show_board()
    print(f"{current_player} win")
if game_tie == True:
    show_board()
    print("Tie")
