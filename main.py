class User:
    role = "User"
    group = "simple user"

    def __init__(self, first_name: str) -> None:
        self.first_name = first_name.title()

    # Определение метода foo()
    def foo(self):

print(User)
