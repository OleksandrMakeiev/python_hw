import math

print("Home Work 16.11.17")
print()
print('--------------------------------------------------------------------------------------------------------')

print("15 Написать функцию, которая отвечает на вопрос, пересекаются ли две заданные окружности на плоскости.\nКаждая окружность задается координатами центра и радиусом.")

def is_intersected(x1, y1, radius1, x2, y2, radius2):
    center_to_center = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if center_to_center <= radius1 + radius2:
        if abs(radius2 - radius1) > center_to_center:
            print('Не пересекаются')
            return False
        else:
            print("Окружности пересекаются")
            return True
    else:
        print('Не пересекаются')
        return False

x1 = int(input("Введите значение координат по оси Х первой окружности: "))
y1 = int(input("Введите значение координат по оси Y первой окружности: "))
x2 = int(input("Введите значение координат по оси Х второй окружности: "))
y2 = int(input("Введите значение координат по оси Y второй окружности: "))
radius1 = int(input("Введите радиус первой окружности: "))
radius2 = int(input("Введите радиус второй окружности: "))
is_intersected(x1, y1, x2, y2, radius1, radius2)