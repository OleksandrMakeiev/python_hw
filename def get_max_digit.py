# 21
import random

number = random.randint(100000000000, 999999999999)
print("Случайное 12-ти значное число:", number)

def get_max_digit(number):
    list = [int(dig) for dig in (str(number))]
    max_digit = max(list)

    return max_digit

print("Самая большая цифра в числе: ", get_max_digit(number))