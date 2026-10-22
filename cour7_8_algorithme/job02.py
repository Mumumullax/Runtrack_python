
def draw_triangle(height):
    
    for i in range(height - 1):

        espaces_debut = " " * (height - 1 - i)
        gauche = "/"
        espaces_milieu = " " * (i * 2)
        droite = "\\"

        print(espaces_debut + gauche + espaces_milieu + droite)
    print("/" + "_" * ())

draw_triangle(5)

#CORRECTION CODE
# cette fonction dessine un triangle de taille "height"
def draw_triangle(size):

    # on itère un nombre de fois egal a la taille, du coup  pour chaque ligne
        for i in range(size):
            space_size = size - i + 1
            print(" " * (space_size - 1) + "/" + " " * (2 * i - 2) + "\\" + " " * (space_size - 1))
                  
        print("/" + " " * (size * 2 - 2) + "\\")

draw_triangle(5)
    

# PSEUDO CODE - CORRECTION
#
# Input utilisateur
# On stock l'input dans une variable pour la taille du triangle (taille = hauteur du triangle)
# nombre de  " " = 2 * taille - 2 > OK
# Si cest la derniere ligne , on affiche les symboles de la derniere ligne en utilisant la formule precedente
# Si on est sur ue ligne au milieu, on utilise la formule precedente pour afficher les espaces
# Le nombre d'espaces avant et apres est egal a la taille - la logne acteulle


# On parcourt chaque ligne du triangle
# i commence à 0 et va jusqu'à height - 1

# 1. Espaces au début :
#    Ils décalent le "/" vers la droite.
#    Plus i augmente, moins il y a d'espaces.
    
# 2. Côté gauche du triangle

# 3. Espaces entre les deux côtés :
#    Ils éloignent le "\" vers la droite.
#    i * 2 donne 0, 2, 4, 6... espaces.

# 4. Côté droit du triangle
# 5. On assemble les éléments et on affiche la ligne

# On appelle la fonction avec une hauteur de 5


