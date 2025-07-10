
# a. Создайте конструктор класса Car. Создайте атрибуты класса Car — color (цвет),
# type (тип), year (год).
# b. Напишите пять методов.
# i. Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
# ii. Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
# iii. Третий — присвоение автомобилю года выпуска.
# Четвертый метод — присвоение автомобилю типа.
# iv. Пятый — присвоение автомобилю цвета.


class Car:
    def __init__(self, color=None, type=None, year=None):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print("Автомобиль заведен")

    def stop(self):
        print("Автомобиль заглушен")

    def set_year(self):
        return print(f"Автомобиль  {self.year} года выпуска")

    def set_type(self):
        return print(f"Автомобиль марки  {self.type}")

    def set_color(self):
        return print(f"Автомобиль имеет {self.color} цвет")

car_obj = Car('красный', '2201', '1997')
car_obj.start()
car_obj.stop()
car_obj.set_year()
car_obj.set_type()
car_obj.set_color()






