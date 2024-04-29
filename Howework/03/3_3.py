# Пользователь вводит Имя, Возраст и Город, сформировать приветственное сообщение путем форматирования 3-мя способами

#variant 1

"""name = input("Введите ваше имя: ")
age = input("Введите ваш возраст: ")
city = input("Введите ваш город: ")

welcom = "Привет, {}! Ваш возраст {}, и вы из {}.".format(name, age, city)
print(welcom)"""

#variant 2
"""
name = input("Введите ваше имя: ")
age = input("Введите ваш возраст: ")
city = input("Введите ваш город: ")

welcom = "Привет, %s! Ваш возраст %s, и вы из %s." % (name, age, city)
print(welcom)"""

#variant 3

name = input("Введите ваше имя: ")
age = input("Введите ваш возраст: ")
city = input("Введите ваш город: ")

welcom = f"Привет, {name}! Ваш возраст {age}, и вы из {city}"
print(welcom)