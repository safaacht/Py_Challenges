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

# print("La meilleur note est : ", maximum)
# print("La mauvaise note est : ", minimum)
# print("La moyenne est : ", moyenne)




notes_etudiants = {"Omar": 15, "Sara": 8, "Yassine": 17, "Imane": 11, "Hamza": 6, "Nadia":
14}

note_sup = {}
note_inf = {}

for student in notes_etudiants :
    if notes_etudiants[student] < 10 :
        note_inf[student] = notes_etudiants[student]
    else :
        note_sup[student] = notes_etudiants[student]    

# print(note_sup)        

length_note_sup = len(note_sup)
length_note_etudiants= len(notes_etudiants)

pourcentage_reussite = (length_note_sup / length_note_etudiants) * 100

print(f" Pourcentage de réussite : {'%6.2f' % pourcentage_reussite} %")