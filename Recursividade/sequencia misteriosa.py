def seqm(num):
    if num == 1:
        return 1
    if num == 2:
        return 1
    if num == 3:
        return 1
    if num == 4:
        return 2
    if num == 5:
        return 2

    return seqm(num-1) + seqm(num-5)





num = int(input())
for i in range(1, num+1):
    print(seqm(i))