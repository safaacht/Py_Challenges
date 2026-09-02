# Filtrer des données
temperatures = [18, 25, 31, 14, 27, 35, 22, 19, 30, 12, 28]

temp1 = []
temp2 = []
temp3 = []

for temp in temperatures :
    if temp <= 25 :
        temp1.append(temp)
    elif 20 <= temp <= 30 :
        temp3.append(temp)    
    else :
        temp2.append(temp)    

print(temp1)        
print(temp3)        
print(f"le nombre de températures supérieures à 30 est : {len(temp2)}")        