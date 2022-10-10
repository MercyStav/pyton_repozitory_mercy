number = int(input("Введите предел последовательности числа Фибоначчи:"))

def Fibonachi(number):
    list = [1, 0, 1]
    for i in range(2, number+1):
        list.append(list[i-1] + list[i])

    for i in range(0, -number+1, -1):
        list.insert(0, list[1] - list[0])

    return list

print(Fibonachi(number))