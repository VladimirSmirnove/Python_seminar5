# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
from itertools import count


# Модуль сжатия данных

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

path_RLE = '/Users/inferno163/Documents/Учеба/ДЗ/2 semestr/Python/Seminar(python)_5.py/4_start_RLE'
RLE_file = open(path_RLE,'r')
res_RLE = RLE_file.read()
print('Первоначальные данные: ' + res_RLE)
RLE_file.close()

encoded_val = rle_encode(res_RLE)
print('Данные после обработки модуля сжатия: ' + encoded_val)

# Модуль восстановления данных

def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode    

path_RLE = '/Users/inferno163/Documents/Учеба/ДЗ/2 semestr/Python/Seminar(python)_5.py/4.1_start_RLE.txt'
RLE_file = open(path_RLE,'r')
res_RLE1 = RLE_file.read()
print('Первоначальные данные: ' + res_RLE1)
RLE_file.close()

decoded_val = rle_decode(res_RLE1)
print('Восстановленные данные: ' + decoded_val)

with open ('/Users/inferno163/Documents/Учеба/ДЗ/2 semestr/Python/Seminar(python)_5.py/4_end_RLE', 'w', encoding='utf8') as file:
         file.write('Данные после обработки модуля сжатия: ' + encoded_val)

with open ('/Users/inferno163/Documents/Учеба/ДЗ/2 semestr/Python/Seminar(python)_5.py/4_end_RLE', 'a+', encoding='utf8') as file:
         file.write('\n'+ 'Восстановленные данные: ' + decoded_val)