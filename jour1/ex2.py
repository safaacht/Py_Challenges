#Calcul du salaire
nom = input("Enter votre nom complet : ")
salaire_horaire = int(input("Enter votre salaire horaire : "))
nbr_heures = int(input("Enter votre nbr d'heures travailler : "))

if nbr_heures > 40 :
    salaire = 40 * salaire_horaire
    difference = nbr_heures - 40
    salaire_final = salaire + difference * 1.5
    print(salaire_final)

else :
    salaire = salaire_horaire * nbr_heures
    print(salaire)    



