#!/usr/bin/python
import string
import random

_chars = string.ascii_letters + string.digits

def random_chars(num):
    return ''.join(random.choice(_chars) for i in range(num))

if __name__ == "__main__":
    import sys
    num = 32
    if len(sys.argv) == 2:
        num = int(sys.argv[1])
        if num <1 or num > 4096:
            print("%s is a wrong number in [1,4096]"%num)
            quit()
    print(random_chars(num));

