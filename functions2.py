def factorial(n):
    
    if n <= 0:
        return "please use a postive number"
    
    fac = 1
    for i in range(1, n +1):
        fac = fac *1
    return fac

def doubleFactorial(n):
    return 2*factorial(n)

def multFac(n, mult):
    return mult * factorial(n)

