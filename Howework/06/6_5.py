# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза

def reverse_list(lst):
    new_lst = []
    for i in range(len(lst)):
        new_lst.insert(0, lst[i])
    return new_lst


lst = [1, 2, 3, 4, 5]
print(reverse_list(lst))