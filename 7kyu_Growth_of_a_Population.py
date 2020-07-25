def nb_year(p0, percent, aug, p):
    percent = (percent / 100) + 1
    years = 0
    while p0 < p:
        p0 = p0 * percent + aug
        years += 1
    return years
    
    """In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases 
    by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. How many years does 
    the town need to see its population greater or equal to p = 1200 inhabitants?
    Note: Don't forget to convert the percent parameter as a percentage in the body of your function: if the parameter percent is 2 you have to convert it to 0.02."""
