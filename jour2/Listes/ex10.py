# Données hétérogènes
donnees = ["Omar", 25, "Casablanca", 15.5, True]
obj = {}
arr = []
for donnee in donnees :
    # print(donnee,":",type(donnee))
    # if type(donnee) in obj :
#         obj[type(donnee)] += 1
#     else :
#         obj[type(donnee)] = 1   

# print(obj) 
    if type(donnee) == int or type(donnee) == float :
        arr.append(donnee)
print(arr)        