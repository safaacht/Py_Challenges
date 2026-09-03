# Liste de Dictionnaires & MiniAnalyse

etudiants = [
 {"nom": "Omar", "age": 22, "note": 15},
 {"nom": "Sara", "age": 21, "note": 17},
 {"nom": "Yassine", "age": 23, "note": 9},
 {"nom": "Imane", "age": 20, "note": 13},
 {"nom": "Hamza", "age": 24, "note": 7}
]

echec = {}
admis = {}
total_note = 0
length = len(etudiants)

for etudiant in etudiants :
    # print(etudiant['nom'])
    if etudiant['note'] < 10 :
        echec[etudiant['nom']] = etudiant['note']
    else :
        admis[etudiant['nom']] = etudiant['note']

    total_note += etudiant['note']

moyenne = total_note / length

notes = [etudiant['note'] for etudiant in etudiants]
maximum = max(notes)
minimum = min(notes)
            
# print(moyenne)
# print(f"la meilleur note {"%.2f" % maximum}")
# print(f"la mauvaise note {"%.2f" % minimum}")


ventes = [
 {"produit": "PC", "categorie": "Informatique", "prix": 8000, "quantite": 2},
 {"produit": "Souris", "categorie": "Accessoire", "prix": 150, "quantite": 10},
 {"produit": "Clavier", "categorie": "Accessoire", "prix": 300, "quantite": 5},
 {"produit": "PC", "categorie": "Informatique", "prix": 8000, "quantite": 1},
 {"produit": "Écran", "categorie": "Informatique", "prix": 2500, "quantite": 3}
]

total_ventes = 0

for vente in ventes :
    total_ventes += vente['prix'] * vente['quantite']

# print(total_ventes)    

cpt = 0
prix_produits = [vente['prix'] for vente in ventes]
produit_cher = max(prix_produits)

for vente in ventes:
    if vente['prix'] == produit_cher:
        cpt += vente['quantite']

# print(cpt)
dic = {}

for vente in ventes :
    if vente['produit'] not in dic:
        dic[vente['produit']] = vente['prix'] * vente['quantite']
    else:
       dic[vente['produit']] += vente['prix'] * vente['quantite']

# print(dic)   

category = {}
for vente in ventes :
    if vente['categorie'] not in category :
        category[vente['categorie']] = 1
    else :
        category[vente['categorie']] += 1    

print(category)    
