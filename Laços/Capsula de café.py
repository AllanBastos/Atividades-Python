CXA_CAPS_P = 10
CXA_CAPS_G = 16
QUANT_TOTAL = 0
QUANT_PROF = 7
XICARA = 0
for i in range(QUANT_PROF):
    Qunt = int(input())
    Tam_cxa = str(input())
    if Tam_cxa == "G" or Tam_cxa == "g":
        QUANT_TOTAL += Qunt*CXA_CAPS_G
    elif Tam_cxa == "P" or Tam_cxa == "p":
        QUANT_TOTAL += Qunt * CXA_CAPS_P
Qunt_Final_cap = QUANT_TOTAL
XICARA += ((Qunt_Final_cap*2)/QUANT_PROF)
print(Qunt_Final_cap)
print(int(XICARA))