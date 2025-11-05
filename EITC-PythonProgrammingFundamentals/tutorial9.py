game = [[0,0,0],
		[0,0,0],
		[0,0,0]]

def game_board(player=0,row=0,col=0,just_display=True):
	
    try:
        if(just_display == False):
            game[row][col] = player
    except IndexError as e:
        print("You must enter row and columns inthe range 0-2",e)
	
	print("*"*30)
	print("   a  b  c")
	for count,row in enumerate(game):
		print(count, row)
		#count +=1
	print("*"*30)
	return game

game = game_board(1,row=1,col=3,just_display=False)

game = game_board(_,row=0,col=0,just_display=True)