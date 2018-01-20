#
# Matthew Epstein
# not_learning.py
# This program creates a 150-character string of what it believes English 
# "looks" like, based on a bogus table of letter-pattern frequency.  
#

import sys
import tqdm
from chain import *
from random import *

NUM_LETTERS = 27


# Creates a bogus frequency table.  The string that is to be produced looks at
# this table as a reference for what an English string should look like when it
# creates itself.  Since the frequency table was created randomly however, the
# string will look quite random as well.
def main():
	my_chain = Chain()
	for i in range(NUM_LETTERS):
		for j in range(NUM_LETTERS):
			for _ in range(randint(0,100)):
				my_chain.addTransition(i,j)	
	print my_chain.toString(0, 150)


if __name__ == '__main__':
	if len(sys.argv) != 1:
		print "Incorrect number of arguments"
		exit(1)
	main()