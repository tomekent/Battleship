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

# Lets place the Boats!!!!

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

for j in range(0,len(Boats_hor)):
	sid = randint(0,len(Boats_hor)-1)		# A random x location
	orient = randint(0,1)
	if orient == 0:
		shape = Boats_hor[sid]
	else:
		shape = Boats_ver[sid]
	count = 1
	while count != 0:	
		base = [randint(0,grid_size-1),randint(0,grid_size-1)] 			# Base point to start drawing shape
		count = 0
		for row in shape:
			newrow = [base[0] + row[0],base[1] + row[1]]
			if newrow[0] >= grid_size or newrow[0] < 0 or newrow[1] >= grid_size or newrow < 0:
				count += 1
			elif board_op[newrow[0]][newrow[1]] == '#':
					count += 1
		
	for row in shape:											# Run for each block of each shape
		newrow = [base[0] + row[0],base[1] + row[1]]
		board_op[newrow[0]][newrow[1]] = '#'						# Make a boat



print "\nLet's play Battleship!\n"
print_board(board,board_op)
		
											
# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
	guess_row = int(raw_input("Guess Row:"))-1
	guess_col = int(raw_input("Guess Col:"))-1

	if board_op[guess_row][guess_col] == "#":
		print "Congratulations! You sunk my battleship!"
		break
	else:
		if (guess_row < 0 or guess_row > grid_size) or (guess_col < 0 or guess_col > grid_size):
		   print "Oops, that's not even in the ocean."
		elif(board[guess_row][guess_col] == "X"):
			print "You guessed that one already."
		else:
			print "You missed my battleship!"
			board[guess_row][guess_col] = "X"
		print (turn + 1)
		print_board(board,board_op)
		
		if turn ==3:
			print "Game Over"