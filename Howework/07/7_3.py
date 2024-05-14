# Реализовать класс Category
# Создать атрибут класса categories
# 3.1 Написать метод класса add принимающий на вход название категории, если такой
# категории в атрибуте класса categories нет, добавить данную категорию в список и вернуть
# индекс вхождения новой категории в списке. Если такая категория уже есть, вызвать
# исключение ValueError
# 3.2 Написать метод класса get принимающий индекс и возвращающий категорию из списка
# категорий на этом индексе, если нет элемента на таком индексе, вызвать исключение
# IndexError
# 3.3 Написать метод класса delete принимающий индекс категории в списке категорий и
# удаляющий элемент из списка категорий на этом индексе, если нет элемента на таком
# индексе, ничего не делать, метод ничего возвращать не должен
# 3.4 Написать метод класса update принимающий индекс категорий и новое название
# категории, если нет элемента на таком индексе, то новая категория должна добавляться с
# учетом того, что имена категорий уникальны, если новое имя категории нарушает
# уникальность в списке категорий, вызвать исключение ValueError


class Category:
    categories = []

    @classmethod
    def add(cls, name: str) -> int:
        if name in cls.categories:
            raise ValueError("Категория уже существует")

        cls.categories.append(name)
        return len(cls.categories) - 1

    @classmethod
    def get(cls, index: int) -> str:
        if index < 0 or index >= len(cls.categories):
            raise IndexError("Индекс выходит за пределы списка категорий")

        return cls.categories[index]

    @classmethod
    def delete(cls, index: int):
        if index < 0 or index >= len(cls.categories):
            return

        del cls.categories[index]

    @classmethod
    def update(cls, index: int, new_name: str):
        if index < 0 or index >= len(cls.categories):
            raise IndexError("Индекс выходит за пределы списка категорий")

        if new_name in cls.categories:
            raise ValueError("Новая категория нарушает уникальность")

        cls.categories[index] = new_name