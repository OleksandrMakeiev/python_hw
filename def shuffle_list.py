# 25
import random

list_to_shuffle = [x for x in range(1, 100, 2)]
print("Начальный список: ", list_to_shuffle)
print()
def shuffle_list(list_to_shuffle):
    random_nuber = random.randint(50, len(list_to_shuffle))
    shuffle_list = random.sample(list_to_shuffle, random_nuber)
    print("Перемешаный список: ", shuffle_list)

    return shuffle_list

shuffle_list(list_to_shuffle)


