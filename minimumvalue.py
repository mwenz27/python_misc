# find minimum value of a list

def myMin(lis):
    return min(lis)

x = [853, 328, 315, 248, 987, 113]

#print(x)
#print(myMin(x))

def myMin2(lis):
    # variable to keep track to of the smallest
    small_number = lis[0]
    #create  a loop to check each element
    for i in lis:
        print(i)
        if i < small_number:
            small_number = i
        #if and element is smaller than the smallest it becomes the smallest
    # 3 return the smallest
    return small_number
print(myMin2(x))