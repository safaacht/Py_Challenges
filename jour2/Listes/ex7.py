# Compter les occurrences
def compterOccurrences(element, liste) :
    cpt=0
    for nbr in liste :
        if nbr == element :
            cpt += 1
    print(cpt)  

L = [7, 23, 5, 23, 7, 19, 23, 12, 29]
compterOccurrences(23, L) # 3
compterOccurrences(7, L) # 2
compterOccurrences(100, L)