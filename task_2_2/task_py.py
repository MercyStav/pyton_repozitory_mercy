from base64 import b16encode


N = int(input("Введи число N, программа покажет набор произведений этого числа: "))
a = 1
b = 1
d = []
while (a <= N):
 b = b * a
 d.append(b)
 a = a + 1
print(d)