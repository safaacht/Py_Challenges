#  Vérification avec assert

lst1=[1, 2, 3, 4, 5]

# def carree(liste) :
#     for l in liste :
#         print( l ** 2)

# print(carree(lst1))

lst2 = [l**2 for l in lst1]
# print(lst2)
lst2.append(36)
# lst1.append(36)

assert len(lst1) == len(lst2) , "Error! the length is different"