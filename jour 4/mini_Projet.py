# Charger et représenter les données
def charger_villes(chemin) :
    villes = []

    ville = {
        'Nom_ville' : ... ,
        'X' : ... ,
        'Y' : ...
        }

    with open(chemin , "r") as file :
        lines = file.readlines()

        for line in lines :
            line_splited = line.strip().rsplit(" ",2)

            ville['Nom_ville'] = line_splited[0]
            ville['X'] = float(line_splited[1])
            ville['Y'] = float(line_splited[2])

            rslt = tuple(ville.values()) 
            villes.append(rslt)

        return villes

        # print(len(villes))
# charger_villes('jour 4/villes.txt') 


# Calcul des distances   
import math

def distance(villeA : float, villeB:float) :

    d = math.sqrt((villeA[1] - villeB[1]) ** 2 +(villeA[2] - villeB[2]) ** 2 )
    print(d)

    
villes = charger_villes("jour 4/villes.txt")

print("%.2f" % distance(villes[7], villes[8]))


            

        

     