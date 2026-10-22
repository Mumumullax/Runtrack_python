nom = "Coeur"
prix_unitaire = 20.0
quantite_stock = 15

print("nom du produits:", nom)
print("prix_unitaire", prix_unitaire, "€")
print("15 :", quantite_stock)

quantite_achat = int(input("combien de produits souhaitez-vous acheter ?"))

if quantite_achat <= quantite_stock: 
   quantite_stock = quantite_stock - quantite_achat
   print("achat effectué !")

else:
    print("stock insuffisant.")

prix_unitaire = prix_unitaire * 1.10 

print("nom du produit:", nom)
print("prix unitaire apres inflation:", round(prix_unitaire, 2), "€")
print("quantité restante :", quantite_stock)