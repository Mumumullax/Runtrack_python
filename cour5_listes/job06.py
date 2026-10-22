L = [1, 2, 3, 4, 5]
print(L)
print(L[1])

def exchange(L):
   L[0], L[4] = L[4], L[0]

exchange(L)
print(L)