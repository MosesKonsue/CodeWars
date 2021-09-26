def ones_counter(inp):
    array = []
    counter = 0
    for i in inp:
        if i == 1:
            counter += 1
        elif i == 0 and counter != 0:
            array.append(counter)
            counter = 0
    if counter !=0:
        array.append(counter)
    return array
  
"""
Tranform of input array of zeros and ones to array in which counts number of continuous ones. If there is none, return an empty array
Example
[1, 1, 1, 0, 1] -> [3,1]
[1, 1, 1, 1, 1] -> [5]
[0, 0, 0, 0, 0] -> []
"""
