print('='*20)
print('10 termos de uma PA')
print('='*20)

t = int(input('Primeiro Termo: '))
r = int(input('Razão: '))

# for i in range(10):
#     if i != 9:
#         print(t, end=' ~> ')
#     else:
#         print(t)
#     t += r

dec = t + (10-1) * r
for i in range(t, dec + r, r):
    print(i, end=' ~> ')
print('acabou')