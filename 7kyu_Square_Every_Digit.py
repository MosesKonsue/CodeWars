def square_digits(num):
    result = []
    num = str(num)
    for i in num:
        result.append(int(i) ** 2)
    result = int(''.join(str(i) for i in result))
    return result
    
"""Welcome. In this kata, you are asked to square every digit of a number.
For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
Note: The function accepts an integer and returns an integer"""
