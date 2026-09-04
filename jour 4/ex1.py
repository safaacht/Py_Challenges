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

# affichage_caracteres()

# Demander une phrase à l’utilisateur et afficher le mot le plus long de cette phrase.
def logueur_mot() :
    text = input("Entre votre text : ")
    text_splited = text.split()

    # choix1
    mot_long= max(text_splited, key = len)
    
    # choix 2

    # maximum = 0
    # mot_long = ""
    # for i in text_splited :
    #     if len(i) >= maximum :
    #         maximum = len(i)
    #         mot_long = i


    # print(mot_long)

# logueur_mot()   

# Demander une chaîne de caractères Ch et afficher le nombre d’occurrences de chaque caractère.
def occurency(Ch) :
    dic = {}

    for i in Ch :
        if i not in dic :
            dic[i] = 1
        else :
            dic[i] += 1    

    print(dic)

occurency("artificial intelligence developer")