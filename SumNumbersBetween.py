a = int(input("Select numbers "))
b = int(input("Select number  "))

total  = 0
print(list(range(a,b+1)))
for i in range(a,b+1):
    total += i
    print(total)