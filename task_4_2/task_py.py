N = int(input('Задайте натуральное число: '))
result = []
p = 2

while p != N:
        if N % p == 0:
            N /= p
            result.append(p)
        else:
            p +=1
else:
    result.append(p)
print(f'Список простых множетелей числа {N} = {result}')