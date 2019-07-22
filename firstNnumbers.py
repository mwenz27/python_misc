#print the sum of the first n numbers


a = int(input("number "))


# declaring 
total = 0
for i in range(a+1):
    temp = total
    number = i
    total += i
    print(f'\t\t  {temp} temp\t number {number}\t  total {total}'.upper())