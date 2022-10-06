from random import randint
n = int(input('Введите число : '))
list = []
for i in range(n):
    list.append(randint(-n, n))
file = open(r"F:\projects\python\homework\task_2_4\file.txt")
position_list = []
for line in file:
    position = int(line.strip())
    position_list.append(position)
result = 1
for j in range(len(list)):
    for k in range(len(position_list)):
        if j == position_list[k]:
            result = result * list[j]
print(f'Произведение элементов на позициях из файла равно {result}')
print(f'Список из N элементов, заполненных числами из промежутка [-N, N]: \n {list}')
print(f'Позиции элементов для вычисления произведения: \n {position_list}')