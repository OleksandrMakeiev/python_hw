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

print()
print('--------------------------------------------------------------------------------------------------------')
print()
print(
    "15 Написать функцию, которая отвечает на вопрос, пересекаются ли две заданные окружности на плоскости.\nКаждая окружность задается координатами центра и радиусом.")

def is_intersected(x1, y1, x2, y2, radius1, radius2):
    if center_to_center > (radius1 + radius2):
        return True
    elif center_to_center < abs(radius1 - radius2):
        return True
    elif abs(center_to_center - (radius1 - radius2)) < 0.1:
        return False
    else:
        return False

x1 = int(input("Введите значение координат по оси Х первой окружности: "))
x2 = int(input("Введите значение координат по оси Х второй окружности: "))
y1 = int(input("Введите значение координат по оси Y первой окружности: "))
y2 = int(input("Введите значение координат по оси Y второй окружности: "))
radius1 = int(input("Введите радиус первой окружности: "))
radius2 = int(input("Введите радиус второй окружности: "))
center_to_center = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
is_intersected(x1, y1, x2, y2, radius1, radius2)

if is_intersected(x1, y1, x2, y2, radius1, radius2):
    print("Точек пересечения нет")
elif center_to_center < abs(radius1 - radius2):
    print("Точек пересечения нет")
elif abs(center_to_center - (radius1 - radius2)) < 0.1:
    print("2 точки пересечения")
else:
    print("Окружности касаются")

print()
print('--------------------------------------------------------------------------------------------------------')
print()
print(
    "16 Два поезда движутся на скорости V1 и V2 навстречу друг другу. Между ними 10 км. пути.\nЧерез 4 км пути первый поезд может свернуть на запасной путь. При заданных скоростях узнать столкнутся ли поезда.")

def is_train_crash(speed1, distance, speed2, distance_train1):
    distance_train2 = distance - distance_train1
    time1 = distance_train1 / speed1
    time2 = distance_train2 / speed2
    if time1 > time2:
        return False
    else:
        return True

speed1 = int(input("Введите скорость первого поезда: "))
speed2 = int(input("Введите скорость второго поезда: "))
distance = 10
distance_train1 = 4
is_train_crash(speed1, distance, speed2, distance_train1)

if is_train_crash(speed1, distance, speed2, distance_train1):
    print("Столкновения избежали.")
else:
    print("Поезда столкнулись!")