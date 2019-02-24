i = j = 1

s = 0

for i in range(39):
    i += 2
    j *= 2
    s += i / j



print("{:.2f}".format(s * 2))
