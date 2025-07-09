# 1. создайте класс прямоугольника.
# a. атрибуты - прямоугольнику можно задать ширину и высоту
# b. методы - реализуйте 2 метода:
# i. расчет площади прямоугольника
# ii. расчет периметра прямоугольника
# c. создайте 3 объекта, рассчитайте площадь и периметр для каждого.
# Результаты выводить в консоль.



class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Создаем 3 объекта
rect1 = Rectangle(5, 3)
rect2 = Rectangle(7, 4)
rect3 = Rectangle(10, 2)

# Рассчитываем и выводим площадь и периметр для каждого
print(f"Прямоугольник 1: площадь = {rect1.square()}, периметр = {rect1.perimeter()}")
print(f"Прямоугольник 2: площадь = {rect2.square()}, периметр = {rect2.perimeter()}")
print(f"Прямоугольник 3: площадь = {rect3.square()}, периметр = {rect3.perimeter()}")








