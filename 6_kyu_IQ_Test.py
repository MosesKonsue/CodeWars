def iq_test(numbers):
    nlist = [int(x) for x in numbers.split()]
    odd = []
    even = []
    track = 0
    counter = 1
    for i in nlist:
        if i % 2 == 0:
            even.append(i)
        elif i % 2 != 0:
            odd.append(i)
    if len(odd) == 1:
        track = odd[0]
    elif len(even) == 1:
        track = even[0]

    for i in nlist:
        if i == track:
            return counter
        else:
            counter += 1
            
            
###Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others.
Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers 
finds one that is different in evenness, and return a position of this number.
