objs = [1,"HELLO", 2.5, "строка", "предложение", True, [1, 2, 3], {"ключ": "значение"}]

for i in range(len(objs) -1, -1, -1):
    if isinstance(objs[i], str):
        objs.pop(i)
print(objs)