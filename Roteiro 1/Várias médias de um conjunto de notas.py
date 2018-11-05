nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
pesoN1 = int(input())
pesoN2 = int(input())
pesoN3 = int(input())

a = (nota1+nota2+nota3)/3
calculoPN = (pesoN1 * nota1 + pesoN2 * nota2 + pesoN3 * nota3)

calculoP = (pesoN1 + pesoN2 + pesoN3)

p = calculoPN/calculoP

h = 3/(1/nota1+1/nota2+1/nota3)

print ("a:",  "{:.1f}" .format(a))

print ("p:",  "{:.1f}" .format(p))

print ("h:",  "{:.1f}" .format(h))
