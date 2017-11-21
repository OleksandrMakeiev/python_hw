# 20
import random
num_limit = 100
lower_bound = (int(input("Введите нижнюю границу поиска ")))
upper_bound = (int(input("Введите верхнюю границу поиска ")))

def diff_even_odd(num_limit, lower_bound, upper_bound):
    even_total_sum = 0
    odd_total_sum = 0
    for i in range(num_limit):
        number = random.randint(lower_bound, upper_bound)
        if number % 2 == 0:
            even_total_sum += number

        else:
            odd_total_sum += number

    return even_total_sum - odd_total_sum
print("Разница сумм составляет %d" % diff_even_odd(num_limit, lower_bound, upper_bound))

