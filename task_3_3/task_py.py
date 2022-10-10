list = [1.1, 1.2, 3.1, 5, 10.01]
print(list)
float_list = []
for i in range(0, len(list)):
    float_list.append(round(list[i]%1, 4))
maximum = 0
minimum = float_list[0]
for i in range(0, len(float_list)):
    if float_list[i] > maximum:
        maximum = float_list[i]
        i += 1
    elif float_list[i] < minimum and   float_list[i] != 0:
        minimum = float_list[i]
        i += 1
diff = maximum - minimum
print("Разница между максимальным и минимальным значениями:", diff)