#создайте Input класс. принимающий один аргумент loc.
#создайте объект  search. выведите значение аргумента loc

class Input:

    def __init__(self, loc):  # атрибуты
        # аргументы
        self.loc = loc


    # создаем экземпляры класса


search = Input('input#loc')
# вызываем метод

print(search.loc)
