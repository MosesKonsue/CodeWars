def solution(s):
    result= []
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    if len(s) % 2 != 0:
        result[-1] = result[-1]+"_"
    return result

"""Task
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_')."""
