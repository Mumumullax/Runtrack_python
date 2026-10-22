# On crée une liste de nombres qui ne sont pas dans l'ordre croissant
L = [7, 11, 42, 39, 2]

# PREMIÈRE BOUCLE : on répète le tri plusieurs fois
# range(5) produit les nombres 0, 1, 2, 3, 4
# Cela permet de refaire plusieurs passages sur la liste
for i in range(5):

    # DEUXIÈME BOUCLE : on compare les nombres deux par deux
    # range(4) produit les nombres 0, 1, 2, 3
    # On s'arrête à 3 car on compare chaque nombre avec le suivant
    for j in range(4):

        # On compare le nombre à l'indice j
        # avec le nombre situé juste après, à l'indice j + 1
        if L[j] > L[j + 1]:

            # Si le nombre de gauche est plus grand que celui de droite,
            # on doit échanger leurs positions.

            # On sauvegarde temporairement le nombre de gauche
            temporaire = L[j]

            # On place le nombre de droite à la place du nombre de gauche
            L[j] = L[j + 1]

            # On place le nombre sauvegardé à la place du nombre de droite
            L[j + 1] = temporaire

# On affiche la liste une fois le tri terminé
print(L)
