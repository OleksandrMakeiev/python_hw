import math
print('Home Work 19.11.17')
print('----------------------------------------------------------------------------------------------')
print()
print('17 Написать функцию решения квадратного уравнения.\nОпределение функции:def solve_quadratic_equation(a, b, c): # return 2 valuespass')
print()

print('Введите значения a, b, c для квадратного уравнения такого типа: ax^2 + bx + c = 0')

def solve_quadratic_equation(a, b, c, none):
    if discriminant > 0:
        return (x1, x2)
    elif discriminant == 0:
        x = -b / (2 * a)
        return (x, none)
    else:
        return (none, none)

a = (float(input("a = ")))
b = (float(input("b = ")))
c = (float(input("c = ")))
discriminant = b ** 2 - 4 * a * c
x1 = (-b + math.sqrt(discriminant)) / (2 * a)
x2 = (-b - math.sqrt(discriminant)) / (2 * a)
solve_quadratic_equation(a, b, c, none)

if discriminant > 0:
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discriminant == 0:
    print("x = %.2f" % x)
else:
    print("Корней нет")