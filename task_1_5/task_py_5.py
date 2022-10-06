from math import sqrt

print('Программа находит растояние между двумя точками в 2D прострнстве')
xA = int(input("Введи координаты точки A\nX: "))
yA = int(input("Y: "))

xB = int(input("Введи координаты точки B\nX: "))
yB = int(input("Y: "))

print(f'Растояние между двумя точками: {round(sqrt((xB - xA)**2 + (yB - yA)**2), 2)}')