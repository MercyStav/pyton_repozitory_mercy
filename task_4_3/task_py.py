numbers = [1, 1, 2, 3, 4, 4, 5, 6, 7, 7, 8]
print (f'Последовательность в которой ищем: {numbers}')
new_numbers = []
for i in numbers:
    if numbers.count(i) == 1:
        new_numbers.append(i)
print (f'Последовательность неповторяющихся элементов: {new_numbers}')