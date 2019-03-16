''' meu codigo '''

def chop(t):
    del t[0]
    del t[-1]
    return t


t = [1, 2, 3, 4]

print(chop(t))

''' do site é identico '''
