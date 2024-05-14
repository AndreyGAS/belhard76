# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка

def neighbors_sums(lst):
  neighbors_sums = []

  neighbors_sums.append(lst[-1] + lst[1])

  for i in range(1, len(lst) - 1):
    neighbors_sums.append(lst[i - 1] + lst[i + 1])

  neighbors_sums.append(lst[0] + lst[-2])

  return neighbors_sums


lst = [1, 2, 3, 4, 5]
print(neighbors_sums(lst))