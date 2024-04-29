a = input("введите текст: ")
dictionary = {}
for letter in a:
    if letter not in dictionary:
        dictionary[letter] = 0
    dictionary[letter] += 1
print(dictionary)