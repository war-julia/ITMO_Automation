#создайте Page класс. принимающий один аргумент url.
#реализуйте метод get(), выводящий url
# создайте объект home  и вызовите get()

class Page:

    def __init__(self, url):  # атрибуты
        # аргументы
        self.url = url

    def get(self):
        print(self.url)


home = Page('https://demoqa.com/')
# вызываем метод

home.get()
