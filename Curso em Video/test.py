# escreva seu codigo aqui #
n = int(input())
primo = False
cont = 0
for i in range(1, n+1):
  if i % 2 != 0:
    cont += 1
if cont == 2:
  primo = True

print(primo)