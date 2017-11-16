import math
print("Home Work 16.11.17")
print()
print('--------------------------------------------------------------------------------------------------------')
print("14. Написать функцию, которая будет проверять четность некоторого числа.")

def is_even (numeric):
    if numeric % 2:
        print("Нечетное число")
    else:
        print("Четное число")

numeric = int(input("Введите целое число: "))
is_even(numeric)

print()
print('--------------------------------------------------------------------------------------------------------')
print()
print("15 Написать функцию, которая отвечает на вопрос, пересекаются ли две заданные окружности на плоскости.\nКаждая окружность задается координатами центра и радиусом.")

def is_interest(center1, center2, radius1, radius2):
    center_to_center = center1 - center2
    radius_sum = radius1 + radius2
    if  radius_sum >= abs(center_to_center):
        print("Окружности пересекаются!")
    else:
        print("Окружности не пересекаются!")

center1 = int(input("Введите центр первой окружности: "))
center2 = int(input("Введите центр второй окружности: "))
radius1 = int(input("Введите радиус первой окружности: "))
radius2 = int(input("Введите радиус второй окружности: "))
is_interest(center1, center2, radius1, radius2)

print()
print('--------------------------------------------------------------------------------------------------------')
print()
print("16 Два поезда движутся на скорости V1 и V2 навстречу друг другу. Между ними 10 км. пути.\nЧерез 4 км пути первый поезд может свернуть на запасной путь. При заданных скоростях узнать столкнутся ли поезда.")

def is_train_crash (speed1, distance, speed2, distance_train1):
    distance_train2 = distance - distance_train1
    time1 = distance_train1 / speed1
    time2 = distance_train2 / speed2
    if time1 < time2:
        print("Столкновения избежали.")
    else:
        print("Поезда столкнулись!")

speed1 = int(input("Введите скорость первого поезда: "))
speed2 = int(input("Введите скорость вервого поезда: "))
distance = 10
distance_train1 = 4
is_train_crash (speed1, distance, speed2, distance_train1)