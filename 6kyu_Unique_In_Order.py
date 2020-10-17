def unique_in_order(iterable):
    nlist = [char for char in iterable]
    rlist = []
    for i in nlist:
        if i not in rlist:
            rlist.append(i)
        elif i in rlist and i != rlist[len(rlist)-1]:
            rlist.append(i)
    return rlist
