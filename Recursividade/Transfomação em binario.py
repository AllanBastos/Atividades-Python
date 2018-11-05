def binario(x):
    if x == 1:
        return '0001'
    if x == 2:
        return '0010'
    return binario(x)**(len(x)-1) + binario(x)**(len(x)-2)
n = int(input())
print(binario(n))