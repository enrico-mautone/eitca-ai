game = [[0,0,0],
		[0,0,0],
		[0,0,0]]

print("*"*30)
print("   a  b  c")
for count,row in enumerate(game):
	print(count, row)
	#count +=1
print("*"*30)


game[0][1] = 1
print("*"*30)
print("   a  b  c")
for count,row in enumerate(game):
	print(count, row)
	#count +=1
print("*"*30)