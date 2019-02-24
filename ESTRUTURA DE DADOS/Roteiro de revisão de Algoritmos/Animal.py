grupo1 = input()
grupo2 = input()
tipo = input()

if grupo1 == "vertebrado":
    if grupo2 == "ave":
        if tipo == "carnivoro":
            print("aguia")
        elif tipo == "onivoro":
            print("pomba")
    elif grupo2 == "mamifero":
        if tipo == "onivoro":
            print("homem")
        elif tipo == "herbivoro":
            print("vaca")

elif grupo1 == "invertebrado":
    if grupo2 == "inseto":
        if tipo == "hematofago":
            print("pulga")
        elif tipo == "herbivoro":
            print("lagarta")
    elif grupo2 == "anelideo":
        if tipo == "hematofago":
            print("sanguessuga")
        elif tipo == "onivoro":
            print("minhoca")

