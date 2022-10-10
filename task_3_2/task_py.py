import random

a = int(input("введите число: "))

def randomArray (x):
    listA = []
    for i in range (x):
        listA.append(random.randint(1,10))
    return listA
def para (list):
    listPara = [] 
    b = len(list)//2 + len(list)%2
    k = -1
    for i in range (b):
        listPara.append(list[i]*list[k])
        i+=1
        k-=1
    return listPara

listTotal = randomArray(a)

print(f"Массив = {listTotal}")
print(f"Произведение пар чисел  = {para(listTotal)}")