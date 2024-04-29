# Заполнить список степенями числа 2 (от 2^1 до 2^n)

n = int(input("введите n: "))
a = []
for i in range(1, n + 1):
    a.append(2 ** i)
print(a)