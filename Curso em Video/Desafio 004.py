algo = input('Digite algo: ')
print(type(algo))
print('É numerico?', algo.isnumeric())
print('É alfanumerico?', algo.isalnum())
print('É decimal', algo.isdecimal())
print('É digito', algo.isdigit())
print('É somente espaços?', algo.isspace())
print('É somente alfabetico', algo.isalpha())
print('Esta capitalizada?', algo.istitle())