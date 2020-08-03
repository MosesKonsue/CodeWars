def order(sentence):
    if sentence == "":
        return ""
    sentence = sentence.split(" ")
    result = []
    for i in sentence:
        result.append(0)
    for i in sentence:
        for char in i:
            if char.isnumeric():
                result[int(char) - 1] = i
    return " ".join(result)


"""Your task is to sort a given string. Each word in the string will contain a single number. This number 
is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain 
valid consecutive numbers."""
