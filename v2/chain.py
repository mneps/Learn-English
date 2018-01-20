#
# Matthew Epstein
# chain.py
# This file creates a frequency table based on the Markov chaining technique.
# It tracks the number of times a specific link follows another link.  The
# class has four public methods: lookup(), lookup_reverse(), addTransition(),
# and toString().
#


from random import *
from tqdm import tqdm


class Chain():

    # Creates the initial frequency table by finding the number of unique
    # strings of length k in the file (called num_strings) and creating a 2D
    # array of size len(num_strings) x len(num_strings).  It also creates a
    # pair of dictionaries which are useful for building the string later on.
    # One of the dictionaries maps each Markov "link" to its ID number, while
    # the other dictionary does the reverse, mapping ID nubmers to links
    def __init__(self, file_string, k):
        strings = []
        length = len(file_string)

        for i in tqdm(range(length)):
            string = ""
            for j in range(k):
                string = string + file_string[(i+j) % length]
            if string not in strings:
                strings = [string] + strings

        strings = sorted(strings)
        self.num_strings = len(strings)
        num_list = [x for x in range(self.num_strings)]
        self.dictionary = dict(zip(strings, num_list))
        self.reverseDict = dict(zip(num_list, strings))

        self.chain = [[0 for x in range(self.num_strings)]
                            for y in tqdm(range(self.num_strings))]


    # The three functions below are all fairly self-explanatory
    def lookup(self, key):
        return self.dictionary.get(key)


    def lookup_reverse(self, key):
        return self.reverseDict.get(key)


    def addTransition(self, ptA, ptB):
        self.chain[ptA][ptB] += 1


    # This function uses the frequency table to create a sequence of all the
    # links that could potentially follow the letter passed to the function.
    # The number of times a link is added to the sequence is dictated by how
    # often it is recorded as following the given link in the frequency table.
    # One link from the sequence is then randomly chosen and returned.
    def __next(self, ptA):
        options = []
        for i in range(self.num_strings):
            if self.chain[ptA][i] != 0:
                options += ([i] * self.chain[ptA][i])

        if options == []:
            return []
        # choice() returns a random element from a non-empty sequence
        return choice(options)


    # This function creates a string of the specified number of steps, starting
    # at a random link.  For each letter, the function calls upon the private
    # __next() function to get the next link in the string.  If at any point
    # there is no link to append to the string, the function will return the
    # string it has recorded thus far.
    def toString(self, steps):
        ptStart = randint(0, self.num_strings-1)
        stringRep = self.lookup_reverse(ptStart)
        for i in range(steps):
            toAppend = self.__next(ptStart)
            if toAppend == []:
                return stringRep
            else:
                stringRep +=  self.lookup_reverse(toAppend)[-1]
                ptStart = toAppend

        return stringRep

        

