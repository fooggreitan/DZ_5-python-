# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.

def czah(arr):
    if arr == "":
        return ""
    encoded = []
    lenght = 1

    for i in range(1, len(arr)):   
        if arr[i] == arr[i-1]:
            lenght +=1
        else:
            encoded.extend([str(lenght), str(arr[i-1])])
            lenght = 1
    
    encoded.extend([str(lenght), str(arr[-1])])

    return "".join(encoded)

def czahz(r):
    if r == "":
        return ""
    decoded = []
    lenght = 0

    for i in r:
        if i.isnumeric():
            lenght = 10*lenght + int(i)
        else:
            decoded.append(lenght*i)
            lenght = 0
    return "".join(decoded)

arr = "aaaaAFDDCCCCaaaaaCEEEEEEEEC55555"
r = czah(arr)
print(f'Кодирование значения - > {r}')
print(f'Декодирование значения - > {czahz(r)}')