# Вывести первые N чисел кратные M и больше K

N = int(input("Введите число N: "))
K = int(input("Введите K: "))
M = int(input("Введите M: "))
list = []
number = K + 1
while len(list) < N:
    if number % M == 0:
        list.append(number)
    number += 1
print(list)
