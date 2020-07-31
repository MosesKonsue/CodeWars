def xo(s):
    x =["x", "X"]
    o = ["o", "O"]
    xcount = 0
    ocount = 0
    for i in s:
        if i in x:
            xcount += 1
        elif i in o:
            ocount += 1
    if xcount == ocount:
        return True
    elif xcount == 0 and ocount == 0:
        return True
    else:
        return False
        
"""Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
Examples input/output:
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false"""
