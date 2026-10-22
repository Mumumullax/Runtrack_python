i = 2

while i <= 1000:
    premier = True
    diviseur = 2 

    while diviseur < i:
        if i % diviseur == 0:
            premier = False
            break

        diviseur = diviseur + 1
    if premier == True:
        print(i)

    i = i+ 1