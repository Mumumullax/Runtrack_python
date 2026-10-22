def cesar(message, decalage):
    # Préparer une chaîne vide pour le résultat
    resultat = ""

    # Parcourir chaque caractère du message
    for lettre in message:

        # Vérifier si le caractère est une lettre minuscule
        if lettre.islower():
            # Transformer la lettre en nombre entre 0 et 25
            position = ord(lettre) - ord("a")
            # Ajouter le décalage et revenir dans l'alphabet si nécessaire
            nouvelle_position = (position + decalage) % 26
            # Transformer le nombre obtenu en lettre
            nouvelle_lettre = chr(ord("a") + nouvelle_position)
            # Ajouter la nouvelle lettre au résultat
            resultat += nouvelle_lettre

        # Même traitement pour les lettres majuscules
        elif lettre.isupper():
            position = ord(lettre) - ord("A")
            nouvelle_position = (position + decalage) % 26
            nouvelle_lettre = chr(ord("A") + nouvelle_position)
            resultat += nouvelle_lettre

        # Conserver les espaces, chiffres et signes de ponctuation
        else:
            resultat += lettre

    # Renvoyer le message transformé
    return resultat


print(cesar("bonjour", 3))
print(cesar("xyz", 3))
print(cesar("Bonjour !", 3))
print(cesar("abc", -1))
