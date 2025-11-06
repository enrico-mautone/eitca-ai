
game = [[2, 1, 0],
        [2, 1, 1],
        [1, 1, 0]]


def check_three_in_a_row(row_elems):
    if (row_elems.count(row_elems[0]) == len(row_elems)) and row_elems[0] != 0:
        return row_elems[0]
    return 0

def winner(game):
    # horizontal win
    for index,row in enumerate(game):
        winner = check_three_in_a_row(row)
        if(winner!=0):
            return (winner,'h',index)
        # vertical win
        column = []
        for col_num in range(len(game)):
            column.append(game[col_num][index])
        winner = check_three_in_a_row(column)
        if(winner!=0):
            return (winner,'v',index)
    return (0,'n',0)


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
    


winner_player,dir,index = winner(game)

print("The Winner is player",winner_player,"row #" if dir == 'h' else "column #",index)