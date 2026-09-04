# Demander à l’utilisateur de saisir un nombre entier n et afficher la factorielle de ce nombre ( n! )

def factorielle(nombre) :
    try:
        if nombre <= 0:
            raise ValueError("Le nombre doit être positif et >0 ")

        result = 1

        for i in range(1, nombre + 1):
            result *= i

        print(result)

    except ValueError as erreur:
        print(erreur)


factorielle(0)