# Написать функцию перевода десятичного числа в двоичное и обратно, без использования функции

def in_binary(number):
    binary = ""
    while number:
        binary = str(number % 2) + binary
        number //= 2
    return binary

def in_denary(denary_number):
    denary = 0
    degree = 0
    for цифра in denary_number[::-1]:
        denary += int(цифра) * (2 ** degree)
        degree += 1
    return denary

denary_number = int(input("Введите десятичное number: "))
binary = in_binary(denary_number)
print("Двоичное представление:", binary)
denary = in_denary(binary)
print("Десятичное представление:", denary)