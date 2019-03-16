def has_duplicates(t):
    v = sorted(t)
    c = False
    for i in range(len(v)-1):
        if v[i] == v[i+1]:
            c = True

    return c


lista = [4, 1, 2, 9, 3, 8]

print(has_duplicates(lista))