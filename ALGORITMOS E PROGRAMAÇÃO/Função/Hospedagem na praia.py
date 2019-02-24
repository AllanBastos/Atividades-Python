def calculaHospedagem(tipo, dias):
    if tipo == "individual":
        total = 125 * dias
    if tipo == 'suite dupla':
        total = 140 * dias
    if tipo == 'suite tripla':
        total = 180 * dias
    if dias >= 3:
        return (total - (total*0.15))
    return total


tipo = input().lower()
dias = int(input())
print(calculaHospedagem(tipo, dias))
