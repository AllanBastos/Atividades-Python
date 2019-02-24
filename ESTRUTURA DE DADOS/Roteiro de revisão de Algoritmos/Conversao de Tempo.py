total = int(input())

h = 0
m = 0
s = 0

while total >= 3600:
    h += 1
    total -= 3600

while total >= 60:
    m += 1
    total -= 60

while total >= 1:
    s += 1
    total -= 1

print("{}:{}:{}".format(h, m, s))