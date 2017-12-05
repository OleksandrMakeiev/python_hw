import random
import string

def gen_password():
    symbol = "_"
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + symbol
    return ''.join(random.choice(chars) for x in range(8))

print(gen_password())