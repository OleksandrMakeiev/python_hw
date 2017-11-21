# 19
import random

num_limit = 100
lower_bound = (int(input("Введите нижнюю границу поиска ")))
upper_bound = (int(input("Введите верхнюю границу поиска ")))


def find_max(num_limit, lower_bound, upper_bound):
    max_number = upper_bound
    for i in range (num_limit):
        number = random.randint(lower_bound, upper_bound)
        if number <= max_number:
            max_number = number
            return max_number
print("Мвксимальное случайное число из поиска равно %d" % find_max(num_limit, lower_bound, upper_bound))