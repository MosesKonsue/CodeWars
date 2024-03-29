def high_and_low(numbers):
    arraypos = 0
    nlist = numbers.split(" ")
    for i in nlist:
        nlist[arraypos] = int(i)
        arraypos += 1
    nlist = sorted(nlist)
    return str(max(nlist)) + " " + str(min(nlist))


"""In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first."""

#Moses notes: Consider using these next time: nn = [int(s) for s in numbers.split(" ")]  
#and: return "%i %i" % (max(nn), min(nn))
