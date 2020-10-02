def create_phone_number(n):
    strlist = []
    for i in n:
        strlist.append(str(i))
    return "("+strlist[0]+strlist[1]+strlist[2]+")"+" "+strlist[3]+strlist[4]+strlist[5]+"-"+strlist[6]+strlist[7]+strlist[8]+strlist[9]



"""Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
Example:

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890" """
