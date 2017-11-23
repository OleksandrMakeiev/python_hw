import random

num_limit = (int(input("Введите количество случайных чисел, которые выберет программа:  ")))
lower_bound = (int(input("Введите нижнюю границу поиска: ")))
upper_bound = (int(input("Введите верхнюю границу поиска: ")))

def find_min_max_diff(num_limit, lower_bound, upper_bound):
    max_number = lower_bound
    min_number = upper_bound
    for i in range(num_limit):
        number = random.randint(lower_bound, upper_bound)
        print('Случайное число: ',number)
        if number > max_number:
            max_number = number
        if number < min_number:
            min_number = number
    min_max_diff = max_number - min_number
    return min_max_diff

print("Разница между максимальным и минимальным числом равна  %d" % find_min_max_diff(num_limit, lower_bound, upper_bound))
