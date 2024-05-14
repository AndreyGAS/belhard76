# Написать класс Taxi
# Конструктор класса принимает атрибуты:
# cars: list[Car] (список экземпляров класса Car)
# 2.1 Реализовать метод find_car
# На вход метода поступают атрибуты: count_passengers, is_baby (количество пассажиров,
# наличие ребенка, примечание: количество пассажиров с учетом ребенка если он есть)
# На основании данных, вернуть объект Car из атрибута cars подходящий по параметрам и
# свободный (is_busy = False), у автомобиля сменить атрибут is_busy на значение True, если
# подходящего автомобиля нет, метод должен возвращать None

class Taxi:
    def __init__(self, cars: list[Car]):
        self.cars = cars

    def find_car(self, count_passengers: int, is_baby: bool) -> Car | None:
        for car in self.cars:
            if car.is_busy:
                continue

            if car.count_passenger_seats >= count_passengers and car.is_baby_seat == is_baby:
                car.is_busy = True
                return car

        return None