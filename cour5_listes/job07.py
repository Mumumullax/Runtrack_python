L = [ 8, 24, 48, 2, 16] #Liste des nombres a verifier

compteur = 0 #compteur initialise a 0

for nombre in L: # parcourt chaque nombre de la liste
    if nombre % 3 == 0: # verfifie si le nombre multiple de 3
        compteur += 1 # ajoute 1 au compteur si c'est vrai

print (compteur)  # affiche le nombre total de multiple de 3