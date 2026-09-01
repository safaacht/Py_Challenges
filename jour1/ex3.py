#Contrôle d'accès à un club privé

age = int(input("Entrer votre age : "))

if age < 18 :
    print("Votre accés est refusée")

elif 18 < age < 25 :
    print("Bienvenue! accées est gratuit")

else:
    reponse = input("Vous etes membre ou accompagnee d'un membre O-N :")

    if reponse == "O":
        print("Bienvenue!")
    elif reponse == "N" :
        print("Oops! Accées refuser")
    else:
        print(" Entre que O ou N")        
        