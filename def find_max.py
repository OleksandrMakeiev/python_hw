# 19
import random

num_limit = int(input("Введите количество случайных чисел, которые выберет программа:  "))
lower_bound = int(input("Введите нижнюю границу поиска: "))
upper_bound = int(input("Введите верхнюю границу поиска: "))

def find_max(num_limit, lower_bound, upper_bound):
    max_number = lower_bound

    for i in range(num_limit):
        number = random.randint(lower_bound, upper_bound)
        print('Случайное число: ',number)
        if number > max_number:
            max_number = number
    return max_number
    print(max_number)

print("Максимальное случайное число из поиска равно %d" % find_max(num_limit, lower_bound, upper_bound))
