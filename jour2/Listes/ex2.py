#  Ajouter et supprimer

langages = ["Python", "Java", "JavaScript", "C++"]

#===========
# === A ====
# ==========

langages.append("PHP")
langages.append("SQL")
langages.insert(2,"C")
# print(langages)

#===========
# === B ====
# ==========

langages.remove("Java")
langages.pop()
print(langages,"\n ", len(langages))