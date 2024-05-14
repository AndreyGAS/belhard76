# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа - пустая строка)

users_name = {
    1: {'name': 'Andrey', 'surname': 'Morozov', 'phone': '44-741-85-96', 'email': 'morozov@gmail.com'},
    2: {'name': 'Masha', 'surname': 'Zaitsev', 'phone': '33-369-25-14', 'email': None},
    3: {'name': 'Vladislava', 'surname': 'Ivanova', 'phone': '44-589-63-21', 'email': ''},
    4: {'name': 'Alexey', 'surname': 'Goroshko', 'phone': '44-587-41-23'},
    5: {'name': 'Misha', 'surname': 'Vecher', 'phone': '33-654-98-32', 'email': 'vecher@gmail.com'}
}


def get_user_wo_email(data: dict):
    for key, value in data.items():
        if not value.get("email"):
            print(value["name"])


get_user_wo_email(users_name)