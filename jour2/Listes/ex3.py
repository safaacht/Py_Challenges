# Analyse des notes
notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]

# for note in notes :
#     print(note)

total = sum(notes)
moyenne = total / len(notes)
# print("%6.2f" % moyenne)


notes_sup_moy = []
notes_inf_moy = []

for note in notes :
    if note < moyenne:
        notes_inf_moy.append(note)
    else :
        notes_sup_moy.append(note)    

# print(notes_inf_moy)        
# print(notes_sup_moy)   

maximum = max(notes)
minimum = min(notes)
# print(f"La meilleur note est : {maximum} \n La mauvaise est : {minimum}")

cpt = 0
for note in notes :
    if note >= 10 :
        cpt += 1

pourcentage = (cpt / len(notes)) * 100
print(cpt , "%6.2f" % pourcentage ,'%')        