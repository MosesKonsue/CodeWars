def sort_array(source_array):
    oddlist = sorted([x for x in source_array if x % 2 != 0])
    counter = 0
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = oddlist[counter]
            counter += 1
    return source_array
    
    
"""You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it."""
