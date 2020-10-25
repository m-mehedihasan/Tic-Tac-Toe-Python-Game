'''
 A Python Tic Tac Toe Game
 Written By Mehedi Hasan
 B.Sc(Hons) in CSE, NU      
'''
#import Section
import os 




#Drawing four hypen 
board = ["____", "____", "____",
		 "____", "____", "____",
		 "____", "____", "____"]

#Global Variable Decalration Section
game_is_over = False 
current_player 	 = "X"


#Function declaration areas
def displayBoard():
	print("|  " + board[0] + "  |  " + board[1] + "  | " + board[2] + "  |\n")
	print("|  " + board[3] + "  |  " + board[4] + "  | " + board[5] + "  |\n")
	print("|  " + board[6] + "  |  " + board[7] + "  | " + board[8] + "  |\n")



def startGame():
	#displaying initial board
	displayBoard()

	while game_is_over == False:

		position		= input(f"({current_player} turn) Choose a position: ")
		clearScreen()
		gameMessage()
		try:
			position 	= int(position)
			if position < 1 or position > 9:
				raise ValueError
			else:
				position = position - 1
		except:
			print("Please choose position from 1 to 9")
			continue
		#Placing current player to the entered position
		board[position] = "_" + current_player + "__"
		displayBoard()
		check_for_winner()
		flip_player()
		



#Fliping the player from x to o
def flip_player():
	#Set up global variables
	global current_player

	temp = current_player
	
	#Changing the current player from x to o or vice-versa
	if current_player == "X":
		current_player = "O"

	elif current_player == "O":
		current_player = "X"
	


#Clearing the current screen
def clearScreen():
	#For linux and MacOs
	if os.name == "posix":
		_= os.system("clear")
	#For windows os
	else:
		_= os.system("cls")


#Winner Checking function
def check_for_winner():
	#Checking tie 
	check_if_tie_occure()

	row_winner 		= check_row_winner()
	column_winner 	= check_column_winner()
	diagonal_winner = check_diagonal_winner()


	#If Game is over find the winner
	if game_is_over:
		#Finding row winner name
		if row_winner != None:
			row_winner = list(row_winner)
			for winner in row_winner:
				if winner == "X":
					print("\n|> Congratulations! X has won. <|")
				elif winner == "O":
					print("\n|> Congratulations! O has won. <|")

		#Finding column winner name
		elif column_winner != None:
			column_winner = list(column_winner)
			for winner in column_winner:
				if winner == "X":
					print("\n|> Congratulations! X has won. <|")
				elif winner == "O":
					print("\n|> Congratulations! O has won. <|")

		#Finding diagonal winner name
		elif diagonal_winner != None:
			diagonal_winner = list(diagonal_winner)
			for winner in diagonal_winner:
				if winner == "X":
					print("\n|> Congratulations! X has won. <|")
				elif winner == "O":
					print("\n|> Congratulations! O has won. <|")

		#End of game_is_over IF



def check_if_tie_occure():
	#Seting up global variable
	global game_is_over

	if "____" not in board:
		game_is_over = True
		print("\n|> Tie Occured! XO Draw.<|")


#Chcking winner in row
def check_row_winner():
	#Set up global variables
	global game_is_over

	row_1	= board[0] == board[1] == board[2] != "____"
	row_2	= board[3] == board[4] == board[5] != "____"
	row_3	= board[6] == board[7] == board[8] != "____"

	#checking game_is_over condition
	if row_1 or row_2 or row_3:
		game_is_over = True

	#Returning the winner
	if row_1:
		return board[0]
	elif row_2:
		return board[3]
	elif row_3:
		return board[6]



#Checking winner in column
def check_column_winner():
	#Set up global variables
	global game_is_over

	column_1	= board[0] == board[3] == board[6] != "____"
	column_2	= board[1] == board[4] == board[7] != "____"
	column_3	= board[2] == board[5] == board[8] != "____"

	#checking game_is_over condition
	if column_1 or column_2 or column_3:
		game_is_over = True

	#Returning the winner
	if column_1:
		return board[0]
	elif column_2:
		return board[1]
	elif column_3:
		return board[2]


#Checking winner in diagonal
def check_diagonal_winner():
	#Set up global variables
	global game_is_over

	diagonal_1	= board[0] == board[4] == board[8] != "____"
	diagonal_2	= board[6] == board[4] == board[2] != "____"
	

	#checking game_is_over condition
	if diagonal_1 or diagonal_2:
		game_is_over = True

	#Returning the winner
	if diagonal_1:
		return board[0]
	elif diagonal_2:
		return board[6]



def gameMessage():
	print("=====> Tic Tac Toe Game (X and 0) Players <=====\n")
	print()

def main():
	gameMessage()
	startGame() #Calling the start game function

if __name__ == '__main__':
	main()

