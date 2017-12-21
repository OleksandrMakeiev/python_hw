#28
import string

str_to_encode = input("Введите фразу для кодировки: ")

def encode(str_to_encode):
    coded_string = ""
    code_method = string.ascii_lowercase + string.digits
    for char in str_to_encode:
        if char not in code_method:
            coded_string += char
            continue

        i = (code_method.index(char) + 5) % len(code_method)
        coded_string += code_method[i]

    return coded_string
print("Закодированная фраза:", encode(str_to_encode))