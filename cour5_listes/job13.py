L: [10, 20, 30, 40, 50, 60, 70, 40, 80, 40, 50] 

def taille (L):
    a = 0
    for i in L:
        a +=1
return a

a=0
doub = []

while a< taille (L):
    if L[a] not in doub :
        doub.append(L[a])
    a+= 1

print(doub)

