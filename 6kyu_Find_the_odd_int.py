def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i


"""Given an array, find the integer that appears an odd number of times.
There will always be only one integer that appears an odd number of times."""
