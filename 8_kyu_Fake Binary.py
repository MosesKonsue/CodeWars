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
