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

    dist = math.sqrt((villeA[1] - villeB[1]) ** 2 +(villeA[2] - villeB[2]) ** 2 )
    return dist

    
# villes = charger_villes("jour 4/villes.txt")

# print("%.2f" % distance(villes[7], villes[8]))


# Heuristique simple pour le Voyageur de Commerce

def itineraire_greedy(villes) :
    itineraire = [villes[0]]
    non_visitees = villes[1:]
    ville_actuelle = villes[0]

    while non_visitees :
        ville_proche = min(non_visitees , key=lambda ville : distance(ville_actuelle , ville))

        itineraire.append(ville_proche)
        non_visitees.remove(ville_proche)
        ville_actuelle = ville_proche

        return itineraire

villes = charger_villes("jour 4/villes.txt")
itineraire = itineraire_greedy(villes)

# for ville in itineraire :
#     print(ville)


# Calcul de la distance totale de la tournée
def distance_totale(itineraire) :
    total = 0

    for i in range(len(itineraire)-1) :
        total += distance(itineraire[i],itineraire[i+1])

    return total    

# distance_totale(itineraire)    


#  Affichage et analyse

print("\n--- Récapitulatif ---")

# nombre total de villes 
print("Nombre total de villes :", len(villes)) 

# itinéraire trouvé 
print("Itinéraire trouvé :") 

for ville in itineraire: 
    print(ville[0]) 

# Distance totale 
print("Distance totale :", distance_totale(itineraire))