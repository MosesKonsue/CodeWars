def get_middle(s):
 divided = int(len(s)/2)
 if len(s) % 2 != 0:
    clist = s[divided:]
    return clist[0]
 elif len(s) % 2 == 0:
  clist = s[divided - 1] + s[divided] 
  return clist
  
"""You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. 
If the word's length is even, return the middle 2 characters.
Examples:
Kata.getMiddle("test") should return "es"
Kata.getMiddle("testing") should return "t"
Kata.getMiddle("middle") should return "dd"
Kata.getMiddle("A") should return "A"
Output should be the middle character(s) of the word represented as a string."""
