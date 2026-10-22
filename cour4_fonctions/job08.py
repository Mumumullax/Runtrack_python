def leo(type, saison):
    if type == "fruits" and saison == "hiver":
        return "orange, mandarine et kiwi"
    elif type == "fruits" and saison == "ete":
        return "poire, fraise, cassis"
    elif type == "legume" and saison == "hiver":
        return "carotte, tapinambour, endive"
    elif type == "legume" and saison == "ete":
        return "artichaud, aubergine, navet"

print (leo("fruits", "ete"))