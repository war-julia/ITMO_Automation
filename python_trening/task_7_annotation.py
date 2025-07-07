#a: int = 5
#b: str = 'строка'
#с: list = [1,2]

#def indent(s: str, width: int) -> str:
   # return " " * (max(0, width - len(s))) + s
#print(indent('123', 123))

def func_len(l: str = '') -> int:
    return len(l)

print(func_len('123'))


def  list_len(a: list,b: list) -> int:
    return max(len(a), len(b))


print(list_len([1, 2, 3],[1, 2, 3, 4, 5]))


def  list_len(a: list, b: int) -> list:
    a.append(b)
    return a


print(list_len([1, 2, 3],4))


def  list_sum(a: list) -> int:  #сумма элементов списка
    return sum(a)


print(list_sum([1, 2, 3, 4, 5]))




