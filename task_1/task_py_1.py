number = int(input('Программа принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.Введите число: '))
if number == 6 or number == 7:
    print("День является Выходным")
elif number > 0 & number < 6:
    print("День является рабочим")
else:
    print("Неверное число")