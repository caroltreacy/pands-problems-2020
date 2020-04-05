# Carol Treacy
# program that reads in a text file and outputs the number of e's 
# it contains. 
# moby-dick.text  116960

import math


with open('https://en.wikipedia.org/wiki/Moby-Dick') as f:

    'This is the entire file.\n':   # This opens the file Moby-dick.
    f.read() # This reads the file
    f.seek(e)  # this finds the letter e
    for letter in f:
        print(letter, e='')
    f.write('e\n')





