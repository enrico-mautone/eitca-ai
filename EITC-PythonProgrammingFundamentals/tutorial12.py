
game = [[2, 1, 1],
        [2, 1, 1],
        [1, 1, 2]]


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
        #reverse diag
        rdiag = []
        for idx,ridx in enumerate(reversed(range(len(game)))):
            rdiag.append(game[idx][ridx])
        winner = check_three_in_a_row(rdiag)
        if (winner != 0):
            return (winner, 'dr', 1)    

    return (0, 'n', 0)


def game_board(player=0, row=0, col=0, just_display=True):
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


winner_player, dir, index = winner(game)


def print_win_message(winner_player, dir, index):
    print(winner_player, dir, index)
    if winner_player == 0:
        return "No winner"
    message = "The Winner is player " + str(winner_player) + " "
    print(dir)
    if dir == 'h':
        message += "row #" + str(index) + " (-)"
    elif dir == 'v':
        message += "column #" + str(index)+ " (|)"
    elif dir == 'dm':
        message += " main diagonal #" + str(index)+ " (\\)"
    elif dir == 'dr':
        message += " reverse diagonal #" + str(index)+ " (/)"

    return message


print(print_win_message(winner_player, dir, index))
