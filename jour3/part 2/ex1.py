# Gestion des exceptions et division

def diviser(a,b) :
    try:
        return a / b


    except ZeroDivisionError :
        print("b must be bigger than 0") 
        return 0.0

    except TypeError :
        print(" insert the right type") 
        return 0.0   
    
    finally:
        print("Opération terminée")


print(diviser(6,3))