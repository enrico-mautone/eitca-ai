import itertools

def check_three_in_a_row(row_elems):
    if (row_elems.count(row_elems[0]) == len(row_elems)) and row_elems[0] != 0:
        return row_elems[0]
    return 0


def winner(game):
    # horizontal win
    for index, row in enumerate(game):
        winner = check_three_in_a_row(row)
        if (winner != 0):
            return (winner, 'h', index)
        # vertical win
        column = []
        for col_num in range(len(game)):
            column.append(game[col_num][index])
        winner = check_three_in_a_row(column)
        if (winner != 0):
            return (winner, 'v', index)
        # diag main win
        diag = []
        for d in range(len(game)):
            diag.append(game[d][d])
        winner = check_three_in_a_row(diag)
        if (winner != 0):
            return (winner, 'dm', 0)
        # reverse diag
        rdiag = []
        for idx, ridx in enumerate(reversed(range(len(game)))):
            rdiag.append(game[idx][ridx])
        winner = check_three_in_a_row(rdiag)
        if (winner != 0):
            return (winner, 'dr', 1)

    return (0, 'n', 0)


def show_game_board(player=0, row=0, col=0, just_display=True):
    try:
        if just_display == False:
            game[row][col] = player
        print("*" * 30)
        print("   a  b  c")
        for count, row in enumerate(game):
            print(count, row)
            # count +=1
        print("*" * 30)
        return game
    except IndexError as e:
        print("You must enter row and columns in the range 0-2", e)
    except NameError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        return game


def print_win_message(winner_player, dir, index):
    if winner_player == 0:
        return "No winner"
    message = "The Winner is player " + str(winner_player) + " "
    if dir == 'h':
        message += "row #" + str(index) + " (-)"
    elif dir == 'v':
        message += "column #" + str(index) + " (|)"
    elif dir == 'dm':
        message += " main diagonal #" + str(index) + " (\\)"
    elif dir == 'dr':
        message += " reverse diagonal #" + str(index) + " (/)"

    return message


play = True
players = [1, 2]
player_choice = itertools.cycle(players)
while play:
    cur_player = next(player_choice)
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    winner_player, dir, index = (0,'n',0)

    for play_idx in range(pow(len(game), len(game))):
        print("Turn",play_idx,"Player",cur_player)
        show_game_board()
        col_choice = int(input(str(cur_player)+"> Select a column (0-2): "))
        row_choice = int(input(str(cur_player)+"> Select a row (0-2): "))
        updated_game_board = show_game_board(cur_player,row_choice,col_choice,just_display=False)
        winner_player, dir, index = winner(updated_game_board)
        if winner_player != 0:   
            break
        cur_player = next(player_choice)

    print(print_win_message(winner_player, dir, index))

    end_game_choice = input("Do you want to play again? (y/n)")

    if end_game_choice == "n":
        play = False



