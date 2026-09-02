#  Base & Modification de Dictionnaires
etudiant = {
 "nom": "Omar", "age": 22,
 "ville": "Casablanca", "note": 15
}

# print(etudiant.items())
# print(etudiant.keys())
# print(etudiant["nom"])
# print(etudiant["age"])
# print(etudiant["note"])
# etudiant["note"] = 17
# etudiant["formation"] = "IA"
# print(etudiant)

# ==================================
# ==================================

produit = {
 "nom": "Ordinateur", "prix": 8500,
 "stock": 12, "categorie":"Informatique"
}

produit["prix"] = 7900
produit["disponible"] = True
produit["marque"] = "Lenovo"
produit.pop("categorie")
del produit["stock"]
print(produit)
