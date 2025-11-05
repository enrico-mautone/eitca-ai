game = [[0,0,0],
		[0,0,0],
		[0,0,0]]

def game_board(player=0,row=0,col=0,just_display=True):
	
	if(just_display == False):
		game[row][col] = player

	print("*"*30)
	print("   a  b  c")
	for count,row in enumerate(game):
		print(count, row)
		#count +=1
	print("*"*30)

game_board(1,row=1,col=2,just_display=False)