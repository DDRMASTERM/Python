# Matthew Conover
# IS 3750
# Final Project: Hangman
import random, logging

import logging

# Set up logging and logger file
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -'
							  ' %(message)s')

fh = logging.FileHandler("hangmanlogfile.log")
fh.setLevel(logging.INFO)

sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)

fh.setFormatter(formatter)
sh.setFormatter(formatter)

# Comment out the addHandler(sh) to turn off logging to screen
logger.addHandler(fh)
# logger.addHandler(sh)

# Defining global variables
wordArray = []
word = ""
chars = []
guesses = 0
guessed = ""
lettersFound = 0
win = False
over = False

# Reading words from file
file_name = "words.txt"
try :
	with open(file_name) as f:
		lines = f.readlines()
		for line in lines:
			wordArray.append(line)
		
except FileNotFoundError:
	logger.warning(f"Source file was not found")
	wordArray.append("edgeworth")
	wordArray.append("ike")
	wordArray.append("lucas")
	wordArray.append("sonic")
	wordArray.append("drake")
	wordArray.append("luigi")
	wordArray.append("banjo")

def start():
	'''Startup and ask if they desire to play again'''
	playing = True
	out = '\nWould you like to play? (y or n) '
	leave = "\nGoodbye"
	played = False
	
	
	# Welcoming player and explaining the rules
	print("\nWelcome to Hangman! Here are the rules: \n" +
	"Either guess one single letter or attempt to guess the entire word."
	"\nGuess 10 letters wrong or guess a wrong word and you lose. \n" +
	"Guess the word or every letter and you win!")
	
	
	# While player is playing or interested in playing
	while playing:
		
		# Take input from user and explain expected inputs
		userIn = input(out)
		
		# convert to lower case if entry is alphabetical
		if userIn.isalpha():
			userIn = userIn.lower()
			
		# User chooses to play
		if userIn == "y":
			main_game()
			played = True
			out = '\nPlay again? (y or n) '
			
		# User is not interested
		elif userIn == "n":
			playing = False
			
		# Input was not valid
		else:
			print("\ninvalid input")
	
	# Add to greeting if they played
	if played:
		leave += ", thanks for playing"
	print(f"{leave}!")
	
def main_game():
	'''The main function of the game'''
	
	# global variables needed for this function
	global word
	global guesses
	global guessed
	global lettersFound
	global chars
	global win
	global over
	
	
	# Assign or reset global variables
	word = wordArray[random.randint(0, len(wordArray))].strip()
	guesses = 10
	lettersFound = 0
	chars = []
	for l in word:
		chars.append("_ ")
	over = False
	guessed = ""
	
	# While game is still active
	while over == False:
		s = "\n"
		for i in chars:
			s+=i
			
		# Display current state of game
		print(s)
		print(f"{guesses} guesses remaining\n")
		
		# Take input for guessing a letter or word
		userIn = input("Guess a letter or the word? (l or w) ")
		
		# Convert input to lower if it is a string
		if userIn.isalpha():
			userIn = userIn.lower()	
			
		# User wishes to guess a letter
		if userIn == "l":
			guess_letter()
				
		# User wishes to guess the word		
		elif userIn == "w":
			win = guess_word()
			over = True
		
		#Invalid user input
		else:
			print("Invalid input")
	
	# Run method if game has ended
	game_over(win)

def guess_letter():
	'''Handles single letter guesses, returns if letter was found'''
	
	# Global variables needed for this method
	global chars
	global guessed
	global guesses
	global lettersFound
	global over
	global win
	
	
	finished = False
	
	# While valid guess needs to be made
	while finished == False:
		wordLocation = 0
		guessOrdered = ""
		
		
		# Prints previous guesses
		a = sorted(guessed)
		for l in a:
			guessOrdered += f" {l}"
		print(f"\nPreviously guessed letters: {guessOrdered}")
		
		# Take user input for guessing a letter
		userIn = input("\nWhat letter do you guess? ")
		
		# Input is a letter
		if userIn.isalpha:
			
			# Convert to lowercase
			userIn = userIn.lower()
		
		# More than one letter
		if len(userIn) != 1:
			print("\nPlease enter only one letter")
		
		# Letter was previously guessed
		elif userIn in guessed:
			print("\nThat letter was already guessed")
		
		# Input is not a letter
		elif userIn.isalpha() == False:
			print("\nPlease enter a letter")
			
		# Valid input
		else:
			
			
			# Add letter to list of guessed letters
			guessed += userIn
			
			# Letter is present in the word
			if userIn in word:
				print("\nThat was a good guess!")
				
				# Check each letter of word
				for l in word:
					
					# Reveal locations of guessed letter in the word
					if l == userIn:
						chars[wordLocation] = f"{l} "
						lettersFound += 1
					wordLocation += 1	
				
					
			
				# All letters were found		
				if lettersFound == len(word):
					s = "\n"
					for i in chars:
						s+=i
					print(s)
					print("You found every letter!\n")
					over = True
					win = True
							
			
			# Letter was not in the word
			else:
				print("\nThat letter was not in the word.")
				guesses -= 1
				
				# Out of guesses
				if guesses == 0:
					print("You are out of guesses\n")
					over = True
					win = False
				
			# Loop is finished
			finished = True		
	
def guess_word():
	'''Handles word guesses and returns if correct'''
	
	guessMade = False
	
	# Guess needs to be made
	while guessMade == False:
		userIn = input("\nWhat is your guess for this word? ")
		
		# User input is alphabetical
		if userIn.isalpha():
			
			# Convert to lowercase
			guess = userIn.lower()
			
			# Guess was correct
			if guess == word:
				print("\nThat was correct! \n")
				win = True
				
			# Guess	was incorrect
			else:
				print("\nThat was incorrect. \n")
				win = False
			
			# Guess has been made
			guessMade = True
		
		# Invalid guess
		else:
			print("\nPlease guess using only letters")
	
	#Return if guess was correct
	return win

def game_over (cond):
	'''returns response based on if game was won or lost'''
	
	# Player won the game
	if cond:
		print("Congratulations, you won!")
		
	# Player lost the game
	else:
		print(f"You lost, better luck next time\nThe word was {word}.")

# Run the game
start()
