# Compréhension de listes
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
carres = [nbr**2 for nbr in nombres]
pairs = [nb for nb in nombres if nb %2 ==0]
supp = [nbr for nbr in nombres if nbr > 5]
print(carres)
print(pairs)
print(supp)
