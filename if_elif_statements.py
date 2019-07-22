import random

number_list = [random.randint(1, 10) for i in range(10)]
print(number_list)

def x():
    num = random.randint(1, len(number_list)-1)
    print(num)
    return num

a = number_list[x()]
b = number_list[x()]
c = number_list[x()]

print(f'a {a} b {b} c {c}')