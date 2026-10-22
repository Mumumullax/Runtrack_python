#FONCTION calculer_distance(nombre_marches, hauteur_marche)

#hauteur_totale = nombre_marches * hauteur_marche

#distance_par_trajet = hauteur_totale * 2

#distance_par_jour = distance_par_trajet * 5 

#distance_par_semaine = distance_par_jour * 7 

#distance_en_metres = distance_par_semaine / 100

#AFFICHER le resultat avec la phrase demandée

#FIN FONCTION

def calculer_distance(nombre_marches, hauteur_marche):
    hauteur_totale = nombre_marches * hauteur_marche

    distance_par_trajet = hauteur_totale * 2
    distance_par_jour = distance_par_trajet * 5
    distance_par_semaine = distance_par_jour * 7 
    distance_en_metres = distance_par_semaine / 100

    print(f"Pour {nombre_marches} marches de {hauteur_marche} cm, le gardien parcourt {distance_en_metres:.2f} m par semaine.")

calculer_distance(100, 20)
