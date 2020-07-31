import math
def is_square(n):
    if n < 0:
        return False
    elif n == 0:
        return True
    elif n % math.sqrt(n) == 0:
        return True
    else:
        return False
        
# There is probably a more elegant way to handle 0 and -n

"""Given an integral number, determine if it's a square number:
In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.
The tests will always use some integral number, so don't worry about that in dynamic typed languages."""
