# Fréquence des éléments
L = [7, 23, 5, 23, 7, 19, 23, 12, 29, 7, 5]

frequence = {}

for i in L :
    if i in frequence :
        frequence[i] += 1

    else :
        frequence[i] = 1    

print(frequence)          
