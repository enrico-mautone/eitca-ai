

game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


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


game = game_board(1, row=1, col=3, just_display=False)

game = game_board(0, row=0, col=0, just_display=True)
