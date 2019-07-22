import random

number_list = [random.randint(1, 10) for i in range(10)]

def x():
    num = random.randint(1, len(number_list)-1)
    #print(num)
    return num

def abc(n):
    for i in range(n):
        a = number_list[x()]
        b = number_list[x()]
        c = number_list[x()]

        print(f'loop {n} \t\t a {a} b {b} c {c}')

        if a > b:
            print('a is greater than b')
        elif a < b:
            print('b is greater than a')
        elif c > b > a:
            print('c is the greatest ')
        else:
            print('this is the last line in the loop')
            
abc(4)

    

    