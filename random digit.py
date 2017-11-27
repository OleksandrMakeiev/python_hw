# 23
import random

print("Программа загадывает целое число от 1 до 10, Ваша задача отдгадать его, следуя подсказкам программы. Для выхода нажми q ")
number = random.randint(1, 11)
while True:

    choice = int(input("Сделай свой выбор [1-10]: "))

    if choice > number:
        print("Меньше")

    elif choice < number:
        print("Больше")
    elif choice == number:
        print("Угадал")
        break
