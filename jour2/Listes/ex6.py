# Rechercher un élément

def rechercheElement(element, liste) :
    trouve = False
    for num in liste:
        if num == element :
            print("Index: ", liste.index(num))
            trouve = True
            break
            
    if trouve == False :
        print(False)       
            
        
        
L = [10, 20, 30, 40, 50]
rechercheElement(30, L)
rechercheElement(100, L)

