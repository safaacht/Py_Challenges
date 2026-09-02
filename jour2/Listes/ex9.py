# Texte ➔ Listes ➔ Comparaison

text1 = input("Entret le premier text : ")
text2 = input("Entret le deuxieme text : ")

text1_splited = text1.split()
# print(text1_splited)
text2_splited = text2.split()

# print(text1_splited)
list1 = []
list2 = []

for word in text1_splited :
    if len(word) > 3 :
        list1.append(word)



for word in text2_splited :
    if len(word) > 3 :
        list2.append(word)

common = set(list1) & set(list2)
print(common)        