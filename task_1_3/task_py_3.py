x = int(input('Программа выдает номер четверти плоскости координат по заданной точки.\nВведите X: '))
while (x == 0):
    x  = int(input('X не может быть равен 0. Введите X повторно: '))
y = int(input('Введите Y: '))
while (y == 0):
    y  = int(input('Y не может быть равен 0. Введите Y повторно: '))

if (x > 0) and (y > 0):
    print(f'Точка (X={x}; Y={y}) находится в первой четверти')
    
elif (x < 0) and (y > 0):
    print(f'Точка (X={x}; Y={y}) находится во второй четверти')
    
elif (x < 0) and (y < 0):
    print(f'Точка (X={x}; Y={y}) находится в третьей четверти')
    
else:
    print(f'Точка (X={x}; Y={y}) находится в четвертой четверти')