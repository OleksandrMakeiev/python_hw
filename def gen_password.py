#29
import random
import string
import re

def gen_password():
    symbol = "_"
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits  + symbol
    while True:
        pswd = ''.join(random.choice(chars) for x in range(8))
        if (re.findall('[A-Z]', pswd)) and (re.findall('[a-z]', pswd)) and (re.findall('[0-9]', pswd)):
            return pswd
print(gen_password())