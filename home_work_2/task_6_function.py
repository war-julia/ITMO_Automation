 # определяем функцию
#def add(x, y):
    # return x + y

 # вызывыем функцию

#print(add(1, 2))

#print(add('I a', 'm a tester'))

#def arg(a, b, c=2, d=3):     # сначала записыватьнеобязательные аргументы
 #   return a + b + c + d

#print(arg(1, 1, 1, 1))

#print(arg(2,2))

#print(arg(2,2, 1))

#print(arg(2, 2, '1', 1))

#def range_arg(a, b, c, d):
    # return a + ' ' + b + ' ' + c + ' ' + d

#print(range_arg('1', '1', '1', '1'))

#print(range_arg('1', '2', d='3', c='4'))

#def task_func(a=(1, 2, 3, 4)):    # функция принимает один аргумент а = (1, 2, 3, 4), возвращает первый элемент этого кортежа
 #   return a[1]

#print(task_func())

def squar_func(radius, pi=3.14159):    # функция принимает два аргумента radius, pi=3.14, возвращает площадь круга
    return (radius**2)*pi

print(squar_func(2))