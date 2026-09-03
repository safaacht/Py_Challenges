def calculer_carre(nombre) :
    """Élève un nombre n au carré."""
    try:
        if nombre < 0:
            raise ValueError
        return nombre ** 2

    except TypeError:
        print("il doit etre un nbr valide") 
    
    
    except ValueError :
        print("Le nombre ne peut pas être négatif")

print(calculer_carre(-2))        