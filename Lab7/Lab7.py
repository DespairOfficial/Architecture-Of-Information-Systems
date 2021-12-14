import random
import string
import os
os.system('CLS')
list = []
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
for i in range(1,21):
    rnd = random.random() *100
    list.append(round(rnd - 50))
print(list)   
listOfNegatives = []
for i in list:
     if (list.index(i)%2==1 and i<0):
         listOfNegatives.append(i)
print("Отрицательные числа на нечетных местах: " + str(listOfNegatives))
listOfLetters = []
for i in range(1,21):
    listOfLetters.append(random.choice(letters))

print(listOfLetters)
counterLower = 0
counterUpper = 0
for i in listOfLetters:
    if(ord(i)>ord('A') and ord(i)<=ord('Z')) or (ord(i)>ord('а') and ord(i)<=ord('я')):
        counterUpper+=1
    elif (ord(i)<=ord('z') and ord(i)>=ord('a')) or (ord(i)>ord('А') and ord(i)<=ord('Я')):
        counterLower+=1
print("Прописных: "+str(counterLower))
print("Строчных: "+str(counterUpper))