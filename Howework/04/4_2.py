# Без использования collections, написать программу, которая будет создавать словарь
# для подсчитывания количества вхождений каждойбуквы в текст введенный с клавиатуры

"""a = input("введите текст: ")
dictionary = {}
for letter in a:
    if letter not in dictionary:
        dictionary[letter] = 0
    dictionary[letter] += 1
print(dictionary)"""

"""text = input()
symbol_counter = {i: text.count(i) for i in text}
print(symbol_counter)"""

user_input = input("введите текст: ")
temp_set = set(user_input) #какие символы в строке
output_dict = {symbol: user_input.count(symbol) for symbol in temp_set}
print(output_dict)