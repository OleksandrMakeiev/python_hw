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
    for c in range (1):
        if first > second  and first > third:
            results = first
            print("-1 cамое частое число и оно встречается ", results)
        elif second > first and second > third:
            results = second
            print("1 cамое частое число и оно встречается ", results)
        elif third > first and third > second:
            results = third
            print("0 cамое частое число и оно встречается ", results)
        else:
            return None
calc_frequency(lst)


