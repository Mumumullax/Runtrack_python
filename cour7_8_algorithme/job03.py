#PSEUDO CODE
#
#Pour chaque note dans la liste
        #Si la note est inférieure à 40
            #Ajouter la note sans modification
        #Sinon
            #Calculer le prochain multiple de 5
            #Si la différence est inférieure à 3
               #Remplacer la note par ce multiple de 5
            #FinSi
            #Ajouter la note au résultat
        #FinSi
    #FinPour
    #Retourner la liste des résultats
#Fin

def arrondir_notes(liste_notes):

    nouvelles_notes = []

    for note in liste_notes:

        if note < 40:
            nouvelles_notes.append(note)

        else:
            
            prochain_multiple = ((note // 5) + 1) * 5

            difference = prochain_multiple - note

            if difference < 3:
                note = prochain_multiple

            nouvelles_notes.append(note)

    return nouvelles_notes

notes = [38, 42, 56, 72, 82, 83, 97]

resultat = arrondir_notes(notes)

print(resultat)

# On crée une liste vide pour les nouvelles notes
# On examine chaque note de la liste
# On calcule le prochain multiple de 5
# On calcule la différence avec ce multiple
# Si la différence est inférieure à 3
# On ajoute la note au résultat
# On renvoie la liste finale
# Exemple de test