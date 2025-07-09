#создайте класс Soda. принимает один аргумент добавку
#в этом классе реализуйте метод  show_my_drink выводящий 'газировка и {ДОБАВКА}'
# в случае наличия добавки , иначе "Обычная газировка"

class Soda:



    def __init__(self, ing=None):      #атрибуты
        self.ing = ing               #аргументы

    def show_my_drink(self):
        if self.ing:
            print(f'Газировка и {self.ing}')
        else:
            print('Обычная газировка')



# создаем экземпляры класса
drink1 = Soda()
drink2 = Soda('малина')


# вызываем метод

drink1.show_my_drink()
drink2.show_my_drink()


