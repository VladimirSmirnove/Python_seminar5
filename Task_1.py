# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


text = '/Users/inferno163/Documents/Учеба/ДЗ/2 semestr/Python/Seminar(python)_5.py/1_start_text_file1.txt'
text_file = open(text,'r')
txt = text_file.read()
print(txt)
text_file.close()

def redak_text(txt):
    txt = list(filter(lambda x: 'абв' not in x, txt.split()))
    return ' '.join(txt)
txt = redak_text(txt)
print (txt)

new_text_file = '/Users/inferno163/Documents/Учеба/ДЗ/2 semestr/Python/Seminar(python)_5.py/1_end_text.txt'
new_text = open(new_text_file,'w')
new_text.write(txt)
new_text.close()


