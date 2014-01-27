import numpy, math									# To oo some maths
from random import randint
grid_size = int(10)

board = []
board_op = []
for x in range(grid_size):
	board.append(["-"] * grid_size)
	board_op.append(["-"] * grid_size) 


def print_board(board,board_op):
	print "Opponents Board:"
	for row in board_op:
		print " ".join(row)

	print "\n", "##"*(grid_size), "\n"
	print "Your Guesses:"

	for row in board:
		print " ".join(row)

def random_row(board):
	return randint(0, len(board) - 1)

def random_col(board):
	return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
# print ship_row
# print ship_col

# Lets place the Boats!!!! Woooo

Boats_hor = [[[0,0],[0,1]], 									# Horizontal line ##
			[[0,0],[0,1],[0,2]],								# Horizontal line ###
			[[0,0],[0,1],[0,2]],								# Horizontal line ###
			[[0,0],[0,1],[0,2],[0,3]],							# Horizontal line ####
			[[0,0],[0,1],[0,2],[0,3],[0,4]] 					# Horizontal line #####
			]
Boats_ver = [[[0,0],[1,0]],					  					# Vertical line ##'
			[[0,0],[1,0],[2,0]],								# Vertical line ###'
			[[0,0],[1,0],[2,0]],								# Vertical line ###'
			[[0,0],[1,0],[2,0],[3,0]],							# Vertical line ####'
			[[0,0],[1,0],[2,0],[3,0],[4,0]]						# Vertical line #####'
			]

Boat_types = [[1,2,"Destroyer"],
			  [2,3,"Submarine"],
			  [3,3,"Cruiser"],
			  [4,4,"Battleship"],
			  [5,5,"Carrier"]
			 ]
Boat_type_count = []
for i in range(5):
	Boat_type_count.append([0,0])
# print Boat_type_count	
	
for j in range(0,len(Boats_hor)):
	orient = randint(0,1)
	if orient == 0:
		shape = Boats_hor[j]
	else:
		shape = Boats_ver[j]
	count = 1
	while count != 0:	
		base = [randint(0,grid_size-1),randint(0,grid_size-1)] 			# Base point to start drawing shape
		count = 0
		# boat_size = 0
		for row in shape:
			newrow = [base[0] + row[0],base[1] + row[1]]
			# boat_size += 1
			if newrow[0] >= grid_size or newrow[0] < 0 or newrow[1] >= grid_size or newrow < 0:
				count += 1
			elif board_op[newrow[0]][newrow[1]] != '-':
				count += 1
	for row in shape:											# Run for each block of each shape
		newrow = [base[0] + row[0],base[1] + row[1]]
		board_op[newrow[0]][newrow[1]] = str(Boat_types[j][0])						# Make a boat



print "\nLet's play Battleships!\n"
print_board(board,board_op)
		
											
# PLAY THE GAME!

for turn in range(10):
	guess_row = int(raw_input("Guess Row:"))-1
	guess_col = int(raw_input("Guess Col:"))-1
	
	Boat_type_count = []
	for i in range(5):
		Boat_type_count.append([0,0])
		
	if (guess_row < 0 or guess_row > grid_size-1) or (guess_col < 0 or guess_col > grid_size-1):
	   print "Oops, that's not even in the ocean."
	
	elif board_op[guess_row][guess_col] != "-": 				# We've Hit Something
		board[guess_row][guess_col] = "o"
		print_board(board,board_op)
		print "Hit!"
		for n in range(grid_size):
			for m in range(grid_size):
				if board[n][m] != "-":
					# print Boat_type_count[int(board_op[n][m])-1][1]
					if Boat_type_count[int(board_op[n][m])-1][1] == 0:
						Boat_type_count[int(board_op[n][m])-1][0] += 1
		# print Boat_type_count
		for j in range(5):
			if Boat_type_count[j][1] == 0:
				if Boat_type_count[j][0] == int(Boat_types[j][1]):
					print "You sunk my %s!" % Boat_types[j][2]
					Boat_type_count[j][1] == 1
				
	else:
		if board[guess_row][guess_col] == "o":
			print "You guessed that one already."
		else:
			print "Miss!"
			board[guess_row][guess_col] = "o"
		# print (turn + 1)
		print_board(board,board_op)
	
		if turn ==3:
			print "Game Over"