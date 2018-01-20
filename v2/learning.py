#
# Matthew Epstein
# learning.py
# This program creates a 150-character string of what it believes English 
# "looks" like, based on a frequency table it creates from a user-specified text
# file.  The user can also specify the "link" length at which the program should
# learn.
#


import sys
from chain import *
from random import *
import re
from tqdm import tqdm


# Turns the text file into a single string that can be analyzed
def read_file(filename):
	if not filename.endswith(".txt") and not filename.endswith(".text"):
		print "File must be a text file"
		exit(1)
	try:
		file = open(filename, 'r')
	except:
		print "File", filename, "does not exist"
		exit(1)
	file_string = " ".join(file) #turn entire file into a single string

	regex = re.compile('[^a-zA-Z ]')
	file_string = regex.sub("", file_string) #keep only alphas and spaces
	file_string = file_string.lower()
	return file_string


# Uses the Chain class to create a frequency table.  The number of letters used
# for learning is based on the k value originally entered by the user.
def create_chain(chain, file_string, k):
	length = len(file_string)

	for i in tqdm(range(length)):
		currSt = ""
		nextSt = ""
		for j in range(k):
			currSt = currSt + file_string[(i+j) % length]
			nextSt = nextSt + file_string[(i+j+1) % length]
		chain.addTransition(chain.lookup(currSt), chain.lookup(nextSt))


# Ensurs the number of letters by which the program will learn by is an integer
# (or an entry that can be cast to an integer)
def handle_k(k):
	try:
		k = int(k)
	except:
		print "k must be of type int"
		exit(1)

	if k < 1:
		print "k must be an integer greater than 0"
		exit(1)
	return k


# Uses the functions above as well as the Chain class to create a frequency
# table based on text file referened.  It then creates a 150-character string,
# using the frequency table to learn what English should look like.
def main(filename, k):
	k = handle_k(k)
	file_string = read_file(filename)
	chain = Chain(file_string, k)
	create_chain(chain, file_string, k)
	print chain.toString(150)


if __name__ == '__main__':
	if len(sys.argv) != 3:
		print "Incorrect number of arguments"
		exit(1)
	main(sys.argv[1], sys.argv[2])
