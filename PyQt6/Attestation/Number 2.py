from statistics import mean


a, b = map(int, input('Введите через пробел ').split())
print(mean([x for x in range(a, b+1) if x % 3 == 0]))