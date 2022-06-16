from itertools import combinations
symbols = "_________"
chars = list(symbols)
winners = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(2,4,6),(0,4,8)]
board = {
    (1, 1) : 0,
    (1, 2) : 1,
    (1, 3) : 2,
    (2, 1) : 3,
    (2, 2) : 4,
    (2, 3) : 5,
    (3, 1) : 6,
    (3, 2) : 7,
    (3, 3) : 8
}
x_grid = []
o_grid = []
x_com = []
o_com = []
x_count = 0
o_count = 0
def count_check():
    global x_com
    x_com += list(combinations(x_grid, 3))
    for element in x_com:
        if element in winners:
            global x_count
            x_count+=1
    global o_com
    o_com += list(combinations(o_grid, 3))
    for element in o_com:
        if element in winners:
            global o_count
            o_count+=1
            
def show_grid():
    border = "---------"
    first_line = "| {} {} {} |".format(chars[0],chars[1], chars[2])
    second_line = "| {} {} {} |".format(chars[3],chars[4], chars[5])
    third_line = "| {} {} {} |".format(chars[6],chars[7], chars[8])
    print(border)
    print(first_line)
    print(second_line)
    print(third_line)
    print(border)
    
def show_result():
    global x_count
    global o_count
    if (abs(len(x_grid) - len(o_grid)) >= 2) or (x_count > 0 and o_count > 0):
        result = "Impossible"
    elif x_count > 0 and o_count == 0:
        result = "X wins"
    elif o_count > 0 and x_count == 0:
        result = "O wins"
    elif x_count == 0 and o_count == 0 and "_" not in chars:
        result = "Draw"
    else:
        result = "Game not finished" 
    return result

players = []
def pick_player(players):
    if players == [] or players[-1] == "O":
        player = "X"
        players.append(player)
        return player
    elif players[-1] == "X":
        player = "O"
        players.append(player)
        return player

def board_fill():
    user_move = input()
    test_input = user_move.replace(" ","")
    if test_input.isalpha():
        print("You should enter numbers!")
        board_fill()
    else:
        coordinate = tuple(int(x) for x in user_move.split(" "))
        if coordinate not in board:
            print("Coordinates should be from 1 to 3!")
            board_fill()
        elif chars[board[coordinate]] != "_":
            print("This cell is occupied! Choose another one!")
            board_fill()
        elif chars[board[coordinate]] == "_":
            player = pick_player(players)
            chars[board[coordinate]] = player
            if player == "X":
                x_grid.append(board[coordinate])
                x_grid.sort()
            elif player == "O":
                o_grid.append(board[coordinate])
                o_grid.sort()
        else:
            board_fill()
            
final = ""
while final != "X wins" or final != "O wins" or final!= "Draw":
    show_grid()
    board_fill()
    count_check()
    final = show_result()
    if final == "X wins" or final == "O wins" or final =="Draw":
        show_grid()
        print(final)
        break
