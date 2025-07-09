#2. Функция на вход получает два произвольных числа. Вывести в консоль наибольшее из чисел.
from python_trening.task_8_if import yes_no


def num_max(num_1, num_2):
    if num_1 > num_2:
        print(num_1)

    else:
        print(num_2)

num_max(17, 10)

#Функция на вход получает два произвольных числа. Вывести в консоль “yes”,
# если они отличаются друг от друга на 135, иначе вывести на экран “No”

def num_dif(num_1, num_2):
    if num_1 > num_2 and (num_1 - 135) >= 0:
        print('yes')
    elif num_2 > num_1 and (num_2 - 135) >= 0:
        print('yes')
    else:
        print('no')

num_dif(135, 136)


#Функция на вход получает произвольное число от 1 до 12 (номер месяца).
# Вывести название сезона года в консоль
# (зима, весна, лето, осень)#

def print_season(month):
    if month == 12 or month == 1 or month == 2:
        print("зима")
    elif month >= 3 and month <= 5:
        print("весна")
    elif month >= 6 and month <= 8:
        print("лето")
    elif month >= 9 and month <= 11:
        print("осень")
    else:
        print("Некорректный номер месяца")


print_season(5)  # выведет "весна"


#Функция на вход получает три произвольных числа. Если все числа больше 10,
# то вывести на экран “yes”, иначе “no”

def check_numbers(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print("yes")
    else:
        print("no")


check_numbers(12, 15, 30)
#check_numbers(10, 11, 13)

#Функция на вход получает список,
# состоящий из 5 произвольных чисел.
# Найти количество положительных чисел среди них.

def count_pos(numbers):
    count = 0
    if numbers[0] > 0:
        count = count + 1
    if numbers[1] > 0:
        count = count + 1
    if numbers[2] > 0:
        count = count + 1
    if numbers[3] > 0:
        count = count + 1
    if numbers[4] > 0:
        count = count + 1
    return count


print(count_pos([1, -2, 3, 0, 5]))



#Функция на вход получает 2 переменные.
#a. Кол-во лет (int)
#b. Кол-во месяцев (int)
#Вывести в консоль количество дней за это время.
# Считать, что в каждом месяце 29 дней.


