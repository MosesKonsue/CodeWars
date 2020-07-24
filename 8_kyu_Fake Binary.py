def fake_bin(x):
    nlist = []
    result = ""
    for i in x:
        if i < "5":
            nlist.append("0")
        else:
            nlist.append("1")
    for i in nlist:
      result += str(i) + ""
    return result

#Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.
