#Function to calculate compound interest	parameters: principal, rate per annum,  years
#Value of bank deposit after 10 years?
#principal: $1000
#rate: 2% per annum (compounded annually) 
#
#Say we put $500 in a 2% interest account for 5 years, and then transferred it to 5% interest
#account for 10 years. How much would we have?


def CompInt(princ, rate, years):
    # define a varible to keep track of money so far
    sum_of_money = princ
    interest = 1 + rate/100
```# print(sum_of_money)
    # make a loop
    for i in range(years):
       sum_of_money = sum_of_money*interest
#       print(int(sum_of_money), i, 'years')
#    print('total sum', sum_of_money)
    return sum_of_money
    
        
    
    
    # return the final amount