# Сделать калькулятор: у пользователя справшивается число, потом действие и второе число

number1 = float(input("Введите число 1: "))
do = input("Введите действие (+, -, *, /): ")
number2 = float(input("Введите число 2: "))

if do == "+":
    result = number1 + number2
elif do == "-":
    result = number1 - number2
elif do == "*":
    result = number1 * number2
elif do == "/":
    result = number1 / number2
else:
    print("Error")

print("Result:", result)