import math
 
print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0")
a = float(input("Введите a = "))
b = float(input("Введите b = "))
c = float(input("Введите c = "))
 
D = b ** 2 - 4 * a * c
print("Дискриминант D = " + str(D))
 
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("x1 =" + str(x1) + "\nx2 = " + str(x2) )
elif D == 0:
    x = -b / (2 * a)
    print("x =" + str(x))
else:
    print("Действительных корней нет")