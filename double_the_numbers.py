import random

f = open("number.txt", 'w')
number = random.randint(0,1000)
print(number, file = f)
f.close()

#Reads a number in from a file
f2 = open("number.txt", 'r')
#Double that number
double = str(int(f2.read())*2)

#Write another file that double that number
f3= open("double_number.txt", 'w')

print(double, file = f3)
f3.close()



