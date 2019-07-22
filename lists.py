import random
myList = [random.randint(1,2000) for i in range(100)]

print(len(myList))

import os

print("Path at terminal when executing this file")
print(os.getcwd() + "\n")

file = '/Users/Wenz/Downloads/python_fundamentals-master/labs/07_file_io/words.txt'

with open(file, encoding='utf-8') as words:
    contents = words.read()
    words = contents.split() #create a list for words

print(len(words))

#for i in words:
#    print(i)