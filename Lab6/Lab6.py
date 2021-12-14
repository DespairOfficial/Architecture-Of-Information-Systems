import datetime
import os
theme = input("Введите тему: ")

text = input ("Введите текст: ")
os.system('CLS')
d = datetime.datetime.now()
date = str(d.day)+ "." + str(d.month)+"." + str(d.year)
print ( date.rjust(300))
print( theme.center(140))
print(text)
words = text.split(' ')
print("Количество слов в тексте: " + str(len(words)))

print("Перевернутый текст: ")
print(text[::-1])

