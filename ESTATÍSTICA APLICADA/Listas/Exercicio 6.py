def is_anagrama(palavra1, palavra2):
    return sorted(palavra1) == sorted(palavra2)





a = 'alu'
b = 'lua'

palav_1 = list(a)
palav_2 = list(b)

print(is_anagrama(palav_1, palav_2))