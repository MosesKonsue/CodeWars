def is_isogram(string):
    string = string.lower()
    for s in string:
        if string.count(s) > 1:
            return False
        elif string == "":
            return True
    return True
    
"""An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that 
determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. 
Ignore letter case."""
