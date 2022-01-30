def move_zeros(array):
    result = []
    counterzero = 0
    for i in array:
        if i != 0 or i is False:
            result.append(i)
        elif i == 0:
            counterzero += 1
    for i in range(counterzero):
        result.append(0)
    return result
    
    

"""Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([False,1,0,1,2,0,1,3,"a"]) # returns[False,1,1,2,1,3,"a",0,0]"""
