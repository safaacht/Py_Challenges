# Documenter une fonction avec une docstring

def compute_list_sum(liste) :

    """ Calcule la somme des nombres pairs présents dans une liste.
        Paramètres ---------- liste : list[int] Une liste contenant des nombres entiers. 
        Retour ------ int La somme de tous les nombres pairs de la liste. 
        Exemples -------- >>> compute_list_sum([1, 2, 3, 4, 5]) 6 >>> 
        compute_list_sum([2, 6, 8]) 16 >>> 
        compute_list_sum([1, 3, 5]) 0 """    

    somme = 0

    for nbr in liste :
        if nbr % 2 == 0:
            somme += nbr
    print(somme)        
          

compute_list_sum([1, 2, 3, 4, 6])