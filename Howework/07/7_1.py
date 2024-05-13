class Car:
    def __init__(self, color, count_passenger_seats, is_baby_seat):
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = False

    def __str__(self):
        return f"Автомобиль:\nЦвет: {self.color}\n" \
               f"Количество пассажирских мест: {self.count_passenger_seats}\n" \
               f"" \
               f"Наличие детского кресла: {self.is_baby_seat}\n" \
               f"Статус: {self.is_busy}"
new_car = Car("black", 5, True)
print(new_car.__str__())