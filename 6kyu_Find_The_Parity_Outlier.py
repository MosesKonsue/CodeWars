def find_outlier(integers):
    evencount = []
    oddcount = []
    for n in integers:
        if n % 2 == 0:
            evencount.append(n)
        elif n % 2 != 0:
            oddcount.append(n)
    if len(evencount) == 1:
        return evencount[0]
    elif len(oddcount) == 1:
        return oddcount[0]
        
"""You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. 
Write a method that takes the array as an argument and returns this "outlier" N.""""
