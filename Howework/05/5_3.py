# Вывести четные числа от 2 до N по 5 в строку

n = int(input("Введите четное число N: "))
c = 0
for i in range(2, n+1, 2):
    print(i, end=" ")
    c += 1
    if c == 5:
        print()
        c = 0