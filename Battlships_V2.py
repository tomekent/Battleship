import numpy, math, sys, time								# Import some libraries
from random import randint

######################################################
# 					Set up the board				 #
######################################################
grid_size = int(10)									
debug_mode = 0			# Set to 1 if you want to see the opponents board
			
board = []
board_op = []
for x in range(grid_size):										# Make 2 blank boards, your guesses and you opponents ship locations
	board.append(["-"] * grid_size)
	board_op.append(["-"] * grid_size) 


def print_board(board,board_op):								# A function to print the board out nicely like a gird.
	if debug_mode == 1:
		header = range(0,grid_size)
		print "#" * 30	
		print "\tOpponents Board:"
		print "#" * 30	
		print "     ",' '.join(map(str, range(1,grid_size+1)))
		print "   ","_ " * (grid_size+1)
		count = 0
		for row in board_op:
			count += 1
			print count," "*(2-len(str(count))),"|", " ".join(row)
		print "\n", "##"*(grid_size), "\n"
	print "#" * 30	
	print "\tYour Guesses: "
	print "#" * 30	
	print "     ",' '.join(map(str, range(1,grid_size+1)))
	print "   ","_ " * (grid_size+1)
	count = 0
	for row in board:
		count += 1
		print count," "*(2-len(str(count))),"|", " ".join(row)
	
	print "\n","#" * 30	


def print_sunk():											# Print record of ships sunk
	print "\n","#" * 30	
	sunk_count = 0
	for k in range(len(Boat_type_count)):
		if Boat_type_count[k][1] == 1:
			print "[X]: %s (len:%s)" %(Boat_types[k][2], str(Boat_types[k][1]))
			sunk_count += 1
		else:
			print "[ ]: %s (len:%s)" %(Boat_types[k][2], str(Boat_types[k][1]))
	print "#" * 30	
	return sunk_count

def print_hit():											# Print HIT in big letters
	print "	 _   _ ___ _____ \n	| | | |_ _|_   _|\n	| |_| || |  | |  \n	|  _  || |  | |  \n	|_| |_|___| |_|  \n"

def print_miss():											# Print MISS in big letters
	print "	 __  __ ___ ____ ____  \n	|  \/  |_ _/ ___/ ___| \n	| |\/| || |\___ \___ \ \n	| |  | || | ___) |__) |\n	|_|  |_|___|____/____/ \n"

def print_title():											# Title stuff
	print "\n"*10
	print "#"*80
	print "#"*80
	print "	 ____    _  _____ _____ _     _____ ____  _   _ ___ ____  ____  \n	| __ )  / \|_   _|_   _| |   | ____/ ___|| | | |_ _|  _ \/ ___| \n	|  _ \ / _ \ | |   | | | |   |  _| \___ \| |_| || || |_) \___ \ \n	| |_) / ___ \| |   | | | |___| |___ ___) |  _  || ||  __/ ___) |\n	|____/_/   \_\_|   |_| |_____|_____|____/|_| |_|___|_|   |____/ \n"
	print "#"*80
	print "#"*32,"Tom Kent  2014","#"*32
	print "#"*80, "\n"*5


###################################################
# 			Lets place the Boats!!!! Woooo
###################################################
Boat_types = [[1,2,"Destroyer"],
			  [2,3,"Submarine"],
			  [3,3,"Cruiser"],
			  [4,4,"Battleship"],
			  [5,5,"Carrier"]
			 ]
			
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
Boat_type_count = []											# Count how many of each have been hit
for i in range(5):
	Boat_type_count.append([0,0])
	
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

def check_shot(guess_row,guess_col):
	
	for i in range(len(Boat_type_count)):
		Boat_type_count[i][0] = 0
			
	if (guess_row < 0 or guess_row > grid_size-1) or (guess_col < 0 or guess_col > grid_size-1):
	   print "Oops, that's not even in the ocean."
	elif board_op[guess_row][guess_col] != "-": 				# We've Hit something
		board[guess_row][guess_col] = "X"
		# print "Hit!"
		print_hit()
		time.sleep(0.5)
		print_board(board,board_op)

		for n in range(grid_size):
			for m in range(grid_size):
				if board[n][m] =='X':
					if Boat_type_count[int(board_op[n][m]) - 1][1] == 0:
						Boat_type_count[int(board_op[n][m]) - 1][0] += 1								
			for j in range(len(Boat_type_count)):
				if Boat_type_count[j][1] == 0:
					if Boat_type_count[j][0] == int(Boat_types[j][1]):
						print "\nYou sunk my %s!\n" % Boat_types[j][2]
						Boat_type_count[j][1] = 1			
	else:
		if board[guess_row][guess_col] != "-":
			print "You guessed that one already."
		else:
			board[guess_row][guess_col] = "o"
			# print "Miss!"
			print_miss()
			time.sleep(0.5)
		# print (turn + 1)
		print_board(board,board_op)

	return board, Boat_type_count




############################################################												
#						 PLAY THE GAME!
############################################################

Boat_type_count = []
for i in range(5):
	Boat_type_count.append([0,0])

print_title()
time.sleep(1.)

print_board(board,board_op)	
print_sunk()

# for turn in range(10):
sunk_count = 0
shot_count = 0
while sunk_count < 5 :
	sunk_count = 0
	print "\nTake a shot:\n"
	############ This is where your algorithm should go! ############### < 
	while True:
		try:
			guess_row = int(raw_input("Guess Row:"))-1
			guess_col = int(raw_input("Guess Col:"))-1
			break
		except (TypeError, ValueError):
			print "Error: Only input numbers"
	################################################################### > 
	new_board, Boat_type_count = check_shot(guess_row,guess_col)
	shot_count += 1
	print "Ships sunk:"
	sunk_count = print_sunk()
	print sunk_count


print "Game Over\n"
print "Shots Taken: %s" % str(shot_count)