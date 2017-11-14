# Home Work 09.11.17

print("Домашнее задание 3 13.11.17")

print()
print("--------------------------------------------------------------------------------------------------------------")

import math
print("11. Написать функцию, которая будет переводить градусы в радианы. Используя эту функцию вывести на экран значения косинусов углов в 60, 45 и 40 градусов.")

def degree_to_radians(degree):
    radians = math.radians(degree)
    return radians

math.cos(degree_to_radians(60))
math.cos(degree_to_radians(40))
math.cos(degree_to_radians(45))

print( math.cos( degree_to_radians( 60 ) ) )
print( math.cos( degree_to_radians( 40 ) ) )
print( math.cos( degree_to_radians( 45 ) ) )

degree_to_radians(60)
degree_to_radians(40)
degree_to_radians(45)

print("--------------------------------------------------------------------------------------------------------------")
print()
print("12 Написать функцию, которая рассчитывает сумму всех цифр некоторого трехзначного числа, введенного пользователем в консоли, без использования операторов цикла. А теперь без строк :)")

def abs_and_add(three_digits_number):

    a = three_digits_number // 100
    b = three_digits_number % 100 // 10
    c = three_digits_number % 10
    add = a + b + c
    print("Сумма всех цифр некоторого трехзначного числа = %d" % (add))
    return  add


abs_and_add(int(input('Введите трехзначное число: ')))

print("--------------------------------------------------------------------------------------------------------------")
print()
print("13 Пользователь вводит длины катетов прямоугольного треугольника. Написать функцию, которая вычислит и выведет на экран площадь треугольника и его периметр.")

def triangle_square_and_perimeter(a, b):
    square = 0.5 * a * b
    c = math.sqrt(a**2 + b**2)
    perimeter = a + b + c
    print("Площадь треугольника равна %.2f\n Периметр треугольника равен %.2f" %(square, perimeter))
    return square, perimeter

a = (int(input("Введите значение первого катета ")))
b = (int(input("Введите значение второго катета ")))
triangle_square_and_perimeter(a,b)