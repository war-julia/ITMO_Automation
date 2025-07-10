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



# 2. Создайте класс Math.
# a. Создайте два атрибута — a и b.
# b. Напишите методы
# i. addition — сложение,
# ii. multiplication — умножение,
# iii. division — деление,
# iv. subtraction — вычитание.
# При передаче в методы параметров a и b с ними нужно производить соответствующие
# действия и печатать ответ.

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return print(f"Сложение: {self.a} + {self.b} = {self.a + self.b}")

    def multiplication(self):
        return print(f"Умножение: {self.a} * {self.b} = {self.a * self.b}")

    def division(self):
        if self.b == 0:
            print("Деление на ноль невозможно")
        else:
            return print(f"Деление: {self.a} / {self.b} = {self.a / self.b}")

    def subtraction(self):
        return print(f"Вычитание: {self.a} - {self.b} = {self.a - self.b}")



math_obj = Math(10, 5)
math_obj.addition()
math_obj.multiplication()
math_obj.division()
math_obj.subtraction()

# 3. откройте страницу https://demoqa.com/text-box
# На странице присутствует сайдбар (меню слева)
# a. Создайте объекты для каждой кнопки 2-го уровня вложенности (“Text Box” и т.п.)
# Для этого опишите класс.
# Каждый объект должен содержать в себе:
# - текст кнопки (пример: “Text Box”)
# - тип - одинаковый для всех “Кнопка”
# - локатор - не заполнять, сделать по умолчанию пустой строкой
# Также на кнопку можно нажать - реализуйте метод.
# Метод возвращает текст “Клик по кнопке { ТЕКСТ КНОПКИ }”
# b. выведите текст для каждой кнопки
# c. вызовите “Клик” для каждой кнопки

class Button:
    def __init__(self, text):
        self.text = text
        self.type = "Кнопка"
        self.locator = ""
# метод
    def click(self):
        return print(f"Клик по кнопке {self.text}")


# Список кнопок 2-го уровня вложенности на https://demoqa.com/text-box
buttons_list = [
    Button("Text Box"),
    Button("Check Box"),
    Button("Radio Button"),
    Button("Web Tables"),
    Button("Buttons"),
    Button("Links"),
    Button("Broken Links - Images"),
    Button("Upload and Download"),
    Button("Dynamic Properties")
]

# Вывести текст каждой кнопки Вызвать метод click для каждой кнопки
for btn in buttons_list:
    print(btn.text)
    print(btn.click())
    print()





