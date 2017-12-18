#26
import random
lst = [random.randint(-1, 1) for i in range(11)]
print(lst)


# print(first, second, third)

def calc_frequency(lst):
    first = lst.count(-1)
    second = lst.count(1)
    third = lst.count(0)
    results = []
    if first == second:
        return None
    elif third == second:
        return None
    elif first == third:
        return None
    elif first > second and first > third:
        results = first
        print("-1 cамое частое число и оно встречается ", results)
        return -1
    elif second > first and second > third:
        results = second
        print("1 cамое частое число и оно встречается ", results)
        return 1
    elif third > first and third > second:
        results = third
        print("0 cамое частое число и оно встречается ", results)
        return 0

calc_frequency(lst)