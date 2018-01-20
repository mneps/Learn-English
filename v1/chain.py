#
# Matthew Epstein
# chain_not_learning.py
# This file creates a frequency table based on the Markov chaining technique.
# It tracks the number of times a specific letter follows another letter.  The
# class has two public methods, addTransition() and toString().
#

from random import *

NUM_LETTERS = 27
LETTERS = list("abcdefghijklmnopqrstuvwxyz ")

class Chain():

	# Initializes the frequency table as a 27 x 27 2D array with every cell
	# set to 0 (27 = 26 letters + the space character).  The value in a cell
	# with row x and column y represents the number of times the y-th letter of
	# the alphabet follows the x-th letter.
    def __init__(self):
        self.chain = [[0 for x in range(NUM_LETTERS)]
                            for y in range(NUM_LETTERS)]


    # Should be self-explanatory
    def addTransition(self, ptA, ptB):
        self.chain[ptA][ptB] += 1


    # This function uses the frequency table to create a sequence of all the
    # letters that could potentially follow the letter passed to the function.
    # The number of times a letter is added to the sequence is dictated by how
    # often it is recorded as following the given letter in the frequency table.
    # One letter from the sequence is then randomly chosen and returned.
    def __next(self, ptA):
        options = []
        for i in range(NUM_LETTERS):
            if self.chain[ptA][i] != 0:
                options += ([i] * self.chain[ptA][i])

        if options == []:
            return []
        # choice() returns a random element from a non-empty sequence
        return choice(options)


    # This function creates a string of the specified number of steps, starting
    # at the specified letter.  For each letter, the function calls upon the 
    # private __next() function to get the next letter of the string.  If at
    # any point there is no letter to append to the string, the function will
    # return the string it has recorded thus far.
    def toString(self, ptStart, steps):
        stringRep = LETTERS[ptStart]
        for i in range(steps):
            toAppend = self.__next(ptStart)
            if toAppend == []:
                return stringRep
            else:
                stringRep = stringRep + LETTERS[toAppend]
                ptStart = toAppend

        return stringRep

        

