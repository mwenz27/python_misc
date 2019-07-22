# 0,1,1,2,3,5

def fib(n):
    # define variable
    prev = 0
    current = 1
    print(prev, end=' ')
    print(current, end=' ')
    sum = 0
    #sum = prev + current
    # use a loop to iterate
    for i in range (2, n):
        temp = current + prev
        print(temp, end=' ')
        prev = current
        current = temp
        
    # Find the next number, upeate the previous 2