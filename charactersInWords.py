# write a function that takes a string and prints each character on a new line
import os
import random

file = '/Users/Wenz/Downloads/python_fundamentals-master/labs/07_file_io/words.txt'

with open(file, encoding='utf-8') as words:
    contents = words.read()
    words = contents.split() #create a list for words

def printChars():
    for i in range(4):
        word = words[random.randint(0, len(words))]
        first_letter = word[0]
        #random_word_related_to_first_letter
        
        #finding first word for in a list using a list
        
        
        print("-------------------", word.upper(), "-------------------",)

        for count, i in enumerate(word, 0):
            print(" "*18, " "*count ,i.upper(), end='\n')
        
                
#printChars()