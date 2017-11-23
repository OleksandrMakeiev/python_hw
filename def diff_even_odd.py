# 20
import random
num_limit = (int(input("Введите количество случайных чисел, которые выберет программа:  ")))
lower_bound = (int(input("Введите нижнюю границу поиска ")))
upper_bound = (int(input("Введите верхнюю границу поиска ")))

def diff_even_odd(num_limit, lower_bound, upper_bound):
    even_total_sum = 0
    odd_total_sum = 0
    for i in range(num_limit):
        number = random.randint(lower_bound, upper_bound)
        #print("Случайное число: ", number)
        if number % 2 == 0:
            even_total_sum += number
            #print("Сумма четных чисел: ", even_total_sum)

        else:
            odd_total_sum += number
            #print("Сумма нечетных чисел: ", odd_total_sum)

    diff_even_odd = even_total_sum - odd_total_sum


    return diff_even_odd
print("Разница сумм составляет %d" % diff_even_odd(num_limit, lower_bound, upper_bound))

