tipo = str(input())

t = float(input())

if tipo=="C" and t >= -273.0:
    f = (t*1.8)+32
    k = t+273.15
    print (("{:.1f}".format(f)), ("F"))
    print (("{:.2f}".format(k)), ("K"))
elif tipo ==  "F" and t >= -459.67:
    c = (t-32)/1.8000
    k = (t+459.67)*5/9
    print (("{:.2f}".format(c)), ("C"))
    print (("{:.3f}".format(k)), ("K"))
elif tipo == "K" and t >= 0.0:
    c = t - 273.15
    f = t * 1.8-459.67
    print (("{:.2f}".format(c)), ("C"))
    print (("{:.2f}".format(f)), ("F"))

else:
    print("Valor de temperatura abaixo do minimo")