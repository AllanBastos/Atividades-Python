''' meu codigo '''

def middle(lista):
    nova = lista[1:-1]
    return nova

t = [1, 2, 3, 4]
print(middle(t))

''' resposta '''

def middle(t):
    """Returns all but the first and last elements of t.

    t: list

    returns: new list
    """
    return t[1:-1]
