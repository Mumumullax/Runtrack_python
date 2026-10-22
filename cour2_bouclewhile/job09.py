n = 1
while n <= 30:
    if n % 2 == 0:
        print (f"{n} est pair")
    else: 
        print (f"{n} est impair")
    n+= 1

    # n = 1 : On initialise le compteur à 1.  
    # while i <= 10 : La boucle continue tant que n est inférieur ou égal à 10.
    # n % 2 == 0 : On utilise l'opérateur modulo (%) pour vérifier si le reste de la division par 2 est égal à 0.
    # Si oui, le nombre est pair.
    # Sinon, le nombre est impair.
    # n += 1 : On augmente n de 1 à chaque tour pour que la condition redevienne fausse et arrêter la boucle.