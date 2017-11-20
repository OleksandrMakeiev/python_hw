import math

print("Home Work 16.11.17")
print()
print('--------------------------------------------------------------------------------------------------------')
print("14. Написать функцию, которая будет проверять четность некоторого числа.")

def is_even(numeric):
    if numeric % 2:
        return True
    else:
        return False

numeric = int(input("Введите целое число: "))
is_even(numeric)
if is_even(numeric):
   print("%d - Нечетное число" % numeric)
else:
    print("%d - Четное число" % numeric)
