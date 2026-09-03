# Construction et Imbrication

noms = ["Python", "SQL", "Pandas", "NumPy"] 
niveaux = [5, 4, 3, 4]

dic = {}

for i , nom in enumerate(noms) :
    for j , niveau in enumerate(niveaux) :
        if i == j :
            dic[nom] = niveau

# print(dic)  


etudiant = {
 "nom": "Omar", "age": 22,
 "formation": {"nom": "Développement IA", "niveau": "Avancé", "duree": 12}
}

etudiant['formation']['niveau'] = "Expert"
etudiant['technologies'] = ["Python", "SQL", "Pandas", "Machine Learning"]

print(etudiant)