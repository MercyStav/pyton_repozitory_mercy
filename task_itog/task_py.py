from sympy import *
import matplotlib.pyplot as plt

print("2. Определить корни")
x = Symbol('x')
func = 5*x**2+10*x-30
y = solve(func)
x1 = round(float(y[0]),2)
x2 = round(float(y[1]),2)
print(x1, x2)

print("2. Найти интервалы, на которых функция возрастает")
fd=diff(func)
print(solve(0<fd))

print("3. Найти интервалы, на которых функция убывает")
print(solve(fd<0))

print("4. Построить график")
list_y = []
for i in range(-5, 6):
    x = i
    y = 5*x**2+10*x-30
    list_y.append(y)
print(list_y)
plt.plot(range(-5, 6), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
plt.plot(range(-5, 6),list_y)
plt.show()

print("5. Вычислить вершину")
corni=solve(fd)
top=corni[0]
x=top
y = 5*x**2+10*x-30
print(top,y)

print("6. Определить промежутки, на котором f > 0")
print(solve(0<func))

print("7. Определить промежутки, на котором f < 0")
print(solve(func<0))