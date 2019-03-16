''' minha resposta '''


def nested_sum(lista):
    soma = 0
    for k in range(len(lista)):
        for j in range(len(lista[k])):
            soma += lista[k][j]
    return soma


t = [[1, 2], [3], [4, 5, 6]]

print(nested_sum(t))

''' resposta do site '''

def nested_sum(t):
    soma = 0
    for nested in t:
        soma += sum(nested)
    return soma


t = [[1, 2], [3], [4, 5, 6]]

print(nested_sum(t))