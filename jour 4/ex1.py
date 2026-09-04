#  Demander à l’utilisateur de saisir un nombre entier n et afficher la factorielle de ce nombre ( n! )

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

# multiplication(2)

# Demander à l’utilisateur un nombre entier L et indiquer s’il s’agit d’un carré parfait.
import math

def racine_carre(nbr) :
    if nbr > 0 :
        rslt = math.sqrt(nbr)
        if rslt.is_integer() :
            print(rslt ,"c'est un carre parfait !")
        else :
            print("naah! ce n'est pas parfait!")   

    else :
        print("plus grand que 0")          
            

# racine_carre(0) 

# Demander une chaîne de caractères à l’utilisateur, puis afficher chaque caractère un par un.
def affichage_caracteres() :
    text = input("Entre votre mot/text : ")
    
    for i in text :
        print(i)

affichage_caracteres()