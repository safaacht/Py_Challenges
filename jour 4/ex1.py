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


# factorielle(0)

# Demander à l’utilisateur un nombre entier m et afficher sa table de multiplication de 1 à 10

def multiplication(num) :
    try :
        if num <= 0 :
            raise ValueError("bigger than 0")

        for i in range(1,11) :
            rslt = i * num
            print(i , " x " , num ," = ", rslt)

    except ValueError as erreur :
        print(erreur)           

multiplication(2)