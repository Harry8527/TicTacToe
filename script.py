"""
Tic tac toe game.

"""
game_state = {
    "player_turn":"Player 1",
    "symbol":"X",
    "turn_counter": True,
    "game_board": []
}


def display_game_board(game_state):
    """
    This function when called will display the current state of the tic tac toe game board.
    """
    print("Current state of the game board:")
    for row in range(board_dimensions):
        for col in range(board_dimensions):
            print(f"| {game_state["game_board"][row][col]} ", end="")
        print("|")
    print("NOTE: This is a 0 based indexing game board, kindly remember that while entering 2D coordinates.")


def set_turn_and_symbol(turn_counter):
    """
    1. Based on the value of turn_counter parameter, we will set the value of turn variable among 
    Player1, and Player2. 
    2. And also set the value for symbol varible among X or O. 
    """
    if turn_counter:
        game_state["player_turn"] = "Player1"
        game_state["symbol"] = "X"
    else:
        game_state["player_turn"] = "Player2" 
        game_state["symbol"] = "O"
        

def check_horizontal(row):
    for index in range(board_dimensions):    
        if game_state['game_board'][row][index] != game_state['symbol'] or game_state['game_board'][row][index] == "-":
            return False
    return True


def check_vertical(col):
    for index in range(board_dimensions):
        if game_state['game_board'][index][col] != game_state['symbol'] or game_state['game_board'][index][col] == "-": 
            return False
    return True


def check_left_diagonal():
    for index in range(board_dimensions):
        if game_state['game_board'][index][index] != game_state['symbol']:
            return False
    return True


def check_right_diagonal():
    for index in range(board_dimensions):
        if game_state['game_board'][index][board_dimensions-index-1] != game_state['symbol']:
            return False
    return True


def check_diagonal():
    """Check for verifying if its an l_diagonal. If the  value on same indexes is the player's symbol, then the
    player could win with left diagonal."""
    
    l_diagonal = False
    r_diagonal = False
    if game_state['game_board'][board_dimensions-2][board_dimensions-2] == game_state['symbol']:
        l_diagonal = check_left_diagonal()

    if game_state['game_board'][0][board_dimensions - 1] == game_state['symbol']:
        r_diagonal = check_right_diagonal()
    print(f"l_diagonal: {l_diagonal}, r_diagonal: {r_diagonal}")
    return l_diagonal or r_diagonal


def check_winner(lastPlayPosition):
    if check_horizontal(row=int(lastPlayPosition[0])) or check_vertical(col=int(lastPlayPosition[1])) or check_diagonal():
        return True
    return False

def check_gamedraw_status():
    for row in range(board_dimensions):
        for col in range(board_dimensions):
            if game_state["game_board"][row][col] != "-":
                continue
            else:
                return False
    return True

def game_logic():
    print(f"It's {game_state["player_turn"]} turn, and he can enter {game_state["symbol"]} on the position of his wish.")
    position = list(
        (
            input(f"{game_state["player_turn"]}, please enter 2D coordinates in a comma separated format: ").split(",")
        )
    )
    #game_state["game_board"][1][1] = 'X'
    if not check_gamedraw_status():
        if game_state["game_board"][int(position[0])][int(position[1])] == "-":
            game_state["game_board"][int(position[0])][int(position[1])] = game_state["symbol"]
            if check_winner(lastPlayPosition=position):
                display_game_board(game_state=game_state)
                print(f"{game_state['player_turn']} wins the game.")
                exit(1)
            display_game_board(game_state=game_state)
            print(f"Value of turn_counter is :{game_state["turn_counter"]}")
            game_state["turn_counter"] = not (game_state["turn_counter"])
            set_turn_and_symbol(turn_counter = game_state["turn_counter"])
            game_logic()
        else:
            print(f"{int(position[0]),int(position[1])} position is already filled with {game_state["game_board"][int(position[0])][int(position[1])]} symbol.Please enter another choice.")
            display_game_board(game_state=game_state)
            game_logic()
    else:
        print("Game is draw")

#player_turn, symbol = set_turn_and_symbol(turn_counter = turn_counter)
board_dimensions = int(input(f"{game_state["player_turn"]}, please enter the dimension for the game: "))
print(f"Board dimensions are set to {board_dimensions} * {board_dimensions} for this tic tac toe game.")

# Declaring a variable,and initialising it with the default value of "-"
game_state["game_board"] = [["-"] * (board_dimensions) for _ in range(int(board_dimensions))]


# Displaying the board, after initializing it.
display_game_board(game_state=game_state)

game_logic()


