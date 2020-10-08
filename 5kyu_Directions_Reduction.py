def dirReduc(arr):
    dict = {"NORTH":"SOUTH","SOUTH":"NORTH","EAST":"WEST","WEST":"EAST"}
    result = []
    for i in arr:
        if result and dict[i] == result[-1]:
            result.pop()
        else:
            result.append(i)
    return result
    


"""Task
Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side)."""
