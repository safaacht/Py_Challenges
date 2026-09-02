#  Parcourir, Analyser et Filtrer

notes = {"Python": 15, "SQL": 13, "JavaScript": 17, "Git": 14, "Linux": 12}
# print(notes.keys())
# print(notes.values())
# print(notes.items())
somme = 0
length = len(notes)

for note in notes :
    somme += notes[note]

maximum = max(notes.values())
minimum = min(notes.values())
moyenne = somme / length  

print("La meilleur note est : ", maximum)
print("La mauvaise note est : ", minimum)
print("La moyenne est : ", moyenne)


