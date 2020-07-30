def digital_root(n):
    result = 0
    recur = 0
    if recur == 0:
        for i in str(n):
            result += int(i)
        recur += 1
    elif recur != 0:
        for i in str(result):
            result += int(i)
    if result >= 10:
        return digital_root(result)
    elif result < 10:
        return result
        
"""Digital root is the recursive sum of all the digits in a number.
Given n, take the sum of the digits of n. If that value has more than one digit, 
continue reducing in this way until a single-digit number is produced. This is only applicable 
to the natural numbers."""
