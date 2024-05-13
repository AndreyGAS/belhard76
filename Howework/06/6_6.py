# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала четные, потом нечётные

def sort_even_odd(lst):
    even_numbers = []
    odd_numbers = []

    for number in lst:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    sorted_list = even_numbers + odd_numbers
    return sorted_list


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sort_even_odd(lst))