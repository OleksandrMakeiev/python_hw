#30
def gen_primes():
    list_of_ints = []
    for x in range(1, 101):
        if x == 1:
            pass
        else:
            for y in list_of_ints:
                if x % y == 0:
                    break
            else:
                list_of_ints.append(x)
    return list_of_ints

print("Все простые числа от 1 до 100 \n", gen_primes())