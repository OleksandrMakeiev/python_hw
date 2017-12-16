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
    if first > second and first > third:
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

    elif (first == second and first !=0) or (second == third and second !=0) or (third == first and third != 0):
        return None
calc_frequency(lst)