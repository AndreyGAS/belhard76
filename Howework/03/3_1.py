# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами

# variant 1
text = "My first home work"
print("My first homework".replace(" ", "--"))

# variant 2
a = 'My first homework'
words = a.split()
b = "--".join(words)
print(b)