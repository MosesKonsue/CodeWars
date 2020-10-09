def pig_it(text):
    initial = text.split()
    result = []
    for i in initial:
        if i.isalpha():
            result.append(i[1:len(i)] + i[0] + "ay")
        else:
            result.append(i)
    return " ".join(result)
    
    
"""Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched."""
