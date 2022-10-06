n = input('Введи вещественное число, программа покажет сумму его чисел: ')
sum = 0
for i in n:
    if i != ',' and i != '.':
        sum += int(i) 
print(sum)