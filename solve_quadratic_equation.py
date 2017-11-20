import math
print('Home Work 19.11.17')
print('----------------------------------------------------------------------------------------------')
print()
print('17 Написать функцию решения квадратного уравнения.\nОпределение функции:def solve_quadratic_equation(a, b, c): # return 2 valuespass')
print()

print('Введите значения a, b, c для квадратного уравнения такого типа: ax^2 + bx + c = 0')

def solve_quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (x1, x2)
    elif discriminant == 0:
        x = -b / (2 * a)
        return (x, None)
    else:
        return (None, None)

a = (float(input("a = ")))
b = (float(input("b = ")))
c = (float(input("c = ")))
solve_quadratic_equation(a, b, c)