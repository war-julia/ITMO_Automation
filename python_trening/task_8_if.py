#программа проверяет, яляется ли число положительным или отрицательным

#num=3

#num=-5
num=0

if num >= 0:
    print('Число больше, либо равно 0')

else:
    print('Число отрицательное')


#str2 содержит в себе str1?


def yes_no (str1,str2):
    if str1 in str2:
        print("ДА")
    else:
        print("НЕТ")


yes_no(str1= 'tist', str2= 'test1')

#num_float= 3.4

#num_float= 0
num_float= -5.8

if num_float > 0:
    print("Положительное число")
elif num_float == 0:
    print("Равно нулю")
else:
    print("Отрицательное число")



permit_print= False
num= 9
if num > 0 and permit_print:
    print("num - Положительное число")
elif not permit_print:
    print("Печать запрещена")



def student_rank(year):
    if year == 1 or year == 2 or year == 3 or year == 4:
        print("Бакалавр")
    elif year == 5 or year == 6:
        print("Магистр")
    elif year == 7 or year == 8 or year == 9:
        print("Аспирант")
    else:
        print("Введите корректный год обучения")

student_rank(3)


def num_rank(num):
    if num < -100 or num > 100:
        print("-")
    else:
        print("+")

num_rank(-20000)

