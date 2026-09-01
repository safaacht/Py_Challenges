#Inverser une chaîne

chain= input("Entrer une chaine de caractere pour l'inverser : ")

length = len(chain)  
chaine_reversed = ""

while length > 0 :
    chaine_reversed += chain[length-1]
    length -= 1

print(chaine_reversed)
