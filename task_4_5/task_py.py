from random import randint
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, -1, -2, -3, -4]
index_list = []
while len(list) != len(index_list):
    index = randint(0, len(list) - 1)
    if index in index_list:
        continue
    index_list.append(index)
result_list = []
for i in range(len(list)):
    result_list.append(list[index_list[i]])
print(result_list)