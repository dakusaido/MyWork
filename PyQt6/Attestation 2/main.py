from arc import plus, minus, division, multiplication


def index_lst(lst, sim):
    index = lst.index(sim)
    if sim == '*':
        lst[index] = multiplication(lst[index - 1], lst[index + 1])
        del lst[index - 1], lst[index]
    elif sim == '/':
        lst[index] = division(lst[index - 1], lst[index + 1])
        del lst[index - 1], lst[index]
    elif sim == '-':
        lst[index] = minus(lst[index - 1], lst[index + 1])
        del lst[index - 1], lst[index]
    elif sim == '+':
        lst[index] = plus(lst[index - 1], lst[index + 1])
        del lst[index - 1], lst[index]


def calc(lst):
    if lst.count('*') > 0:
        index_lst(lst, '*')
        calc(lst)
    elif lst.count('/') > 0:
        index_lst(lst, '/')
        calc(lst)
    elif lst.count('-') > 0:
        index_lst(lst, '-')
        calc(lst)
    elif lst.count('+') > 0:
        index_lst(lst, '+')
        calc(lst)
    return lst[0]


while True:
    numbers_list = input('Введите числа и операции через пробел!!!: ')
    list_numbers = numbers_list.split()
    if list_numbers[-1] in ['+', '-', '/', '*']:
        del list_numbers[-1]

    print(calc(list_numbers))
    print(eval(numbers_list))
