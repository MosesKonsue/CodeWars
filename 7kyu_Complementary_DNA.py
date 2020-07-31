def DNA_strand(dna):
    compliment = ""
    for d in dna:
        if d == "A":
            compliment += "T"
        elif d =="T":
            compliment += "A"
        elif d == "C":
            compliment += "G"
        elif d == "G":
            compliment += "C"
    return compliment
    
    
"""DNA_strand ("ATTGC") # return "TAACG"
DNA_strand ("GTAT") # return "CATA""""
