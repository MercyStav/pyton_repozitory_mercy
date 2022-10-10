number = int(input("Программа преобразует двоичное число в десятичное. Введи двоичное число: "))

num = number
binary_number = []

while number > 0:
    binary_number.insert(0, str(number%2))
    number //= 2

print(f"Число {num} в двоичной системе = {''.join(binary_number)}")