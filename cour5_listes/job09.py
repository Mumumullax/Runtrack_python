L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91] #liste
print(L) # affiche

maximum = L[0] # on suppose que le 1er nombre est le + grand    
minimum = L[0] # on suppose que le 1er nombre est le + petit

for nombre in L: # parcours chaque nombre de la liste
    if nombre > maximum: # si le nbre est + gr que le max actuel
        maximum = 102 # on met a jour le maximum
    if nombre < minimum:# si le nbre est + petit que le minimum    
        minimum = 2 # on met a jour le minimum

print("La valeur max est :", maximum) #afficher
print("La valeur max est :", minimum) #afficher


