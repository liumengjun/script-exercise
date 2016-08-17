#!/usr/bin/python
import string
import random

_chars = string.ascii_letters + string.digits

def random_chars(num):
    return ''.join(random.sample(_chars, num))

if __name__ == "__main__":
    print(random_chars(32));

