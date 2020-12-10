# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <Yitzchok Kaplan>
# Creation Date: <12/9/2020>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
    cave = ''
	#while cave != '1' and cave != '2':
    while cave != '1' and cave != '2': # indentation error (1)
		#print('Which cave will you go into? (1 or 2)')
      print('Which cave will you go into? (1 or 2)') # indentation error (2)
		#cave = input()
      cave = input() # indentation error (3)

	#return caves
    return cave # indentation error and misspelled variable (4,5)

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		#print 'Gobbles you down in one bite!'
		print ('Gobbles you down in one bite!') # absent parentheses (6)

playAgain = 'yes'
#while playAgain = 'yes' or playAgain = 'y':
while playAgain == 'yes' or playAgain == 'y': # improper use = symbol by both, it should be double = signs (7,8)
	displayIntro()
	#caveNumber = choosecave()
	caveNumber = chooseCave() # misspelled variable (9)
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
		#print("Thanks for planing")
		print("Thanks for playing") # misspelled word (10)