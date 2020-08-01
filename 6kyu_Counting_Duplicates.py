def duplicate_count(text):
    text = text.lower()
    count = 0
    dupli = []
    for i in text:
        if text.count(i) > 1 and i not in dupli:
            count += 1
            dupli.append(i)
    print(text)
    return count
    
    
"""Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits
that occur more than once in the input string. The input string can be assumed to contain only alphabets (both 
uppercase and lowercase) and numeric digits."""
