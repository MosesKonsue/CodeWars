def tickets(people):
    cashier = {
        "twentyfive":0,
        "fifty":0,
        "hundred":0
    }
    for i in people:
        if i == 25:
            cashier["twentyfive"] += 1
        elif i == 50:
            cashier["fifty"] +=1
            cashier["twentyfive"] -= 1
            if cashier["twentyfive"] < 0:
                return "NO"
        elif i == 100:
            cashier["hundred"] += 1
            if cashier["fifty"] > 0 and cashier["twentyfive"] > 0:
                cashier["fifty"] -= 1
                cashier["twentyfive"] -=1
            else:
                cashier["twentyfive"] -= 3
            if cashier["fifty"] <0 or cashier["twentyfive"] <0:
                return "NO"
    return "YES"
    
    
    
"""The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line.
Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.
Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.
Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?
Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO."""
