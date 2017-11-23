# 18
first = input("Введите первый символ ")
last = input("Введите последний символ ")
def sum_symbol_codes(first, last):
    first_symbol = ord(first)
    last_symbol = ord(last)
    sum_symbol = 0
    if first_symbol <= last_symbol:
        min_value = min(first_symbol, last_symbol)
        max_value = max(first_symbol, last_symbol)
        # min_value = first_symbol
        # max_value = last_symbol
    # else:
    #     min_value = last_symbol
    #     max_value = first_symbol
    for i in range (min_value, max_value +1):
            sum_symbol += i
    return sum_symbol

print("Сумма введенных символов равна %d" % sum_symbol_codes(first, last))



