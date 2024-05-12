# Дан list чисел на вход поступает число N, необходимо сместить list на указанное число
def move_list(list, n):

  new_list = []

  for i in range(len(list)):
    new_list.append(list[(i + n) % len(list)])
  return new_list

list = [1, 2, 3, 4, 5, 6, 7]
n = 4
new_list = move_list(list, n)
print(new_list)