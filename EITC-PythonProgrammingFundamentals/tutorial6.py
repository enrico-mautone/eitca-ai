game = [[0,0,0],
		[0,0,0],
		[0,0,0]]

def game_board():
	print("*"*30)
	print("   a  b  c")
	for count,row in enumerate(game):
		print(count, row)
		#count +=1
	print("*"*30)

game_board()
game[0][1] = 1
game_board()