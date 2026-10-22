n = int(input("choisis un nombre superieur à zéro (N) :"))
 # tu demandes un nombre à l'utilisateur et tu le convertis en entier.
for i in range(1, n + 1):
    #afficher la table de 1 ; tu parcours les tables de 1 jusqu'au nombre saisi.
    for j in range (1,11):
    # afficher le calcul de 1 multiplié par j ;
    # tu parcours les multiplicateurs de 1 à 10.
        print(i, "x", j, "=", i * j)
        #calcul des deux, et affichage i affiche 2. "x" affiche la lettre x.
        # j affiche 3. "=" affiche le signe égal. i * j calcule et affiche 6.
        

