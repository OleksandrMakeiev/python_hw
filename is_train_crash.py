import math
print("16 Два поезда движутся на скорости V1 и V2 навстречу друг другу. Между ними 10 км. пути.\nЧерез 4 км пути первый поезд может свернуть на запасной путь. При заданных скоростях узнать столкнутся ли поезда.")

def is_train_crash(speed1, speed2):
    distance = 10
    distance_train1 = 4
    distance_train2 = distance - distance_train1
    time1 = distance_train1 / speed1
    time2 = distance_train2 / speed2
    if time1 >= time2:
        return True
    else:
        return False

speed1 = int(input("Введите скорость первого поезда: "))
speed2 = int(input("Введите скорость второго поезда: "))
is_train_crash(speed1, speed2)

if is_train_crash(speed1, speed2):
    print("Поезда столкнулись")
else:
    print("Столкновения избежали.")