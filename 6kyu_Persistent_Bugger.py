import operator
import functools
def persistence(n, counter = 0):
    if (n < 10):
        return counter
    else:
        listnumber = [int(digit) for digit in str(n)]
        result = (functools.reduce(operator.mul,listnumber))
        counter +=1
        if result < 10:
            return counter
        else:
            return persistence(result, counter)
            
"""Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
which is the number of times you must multiply the digits in num until you reach a single digit."""
