import random

def gen_password():
    upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
    lower = "qwertyuiopasdfghjklzxcvbnm"
    digits = "0123456789"
    symbol = "_"

    chars = upper + lower + digits + symbol
    size = random.randint(8, 8)
    return ''.join(random.choice(chars) for x in range(size))

print(gen_password())