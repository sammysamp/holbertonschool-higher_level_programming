#!/usr/bin/python3
def uppercase(str):
    for c in str:
        n = ord(c)
        if n > 96 and n < 123:
            print("{:c}".format(chr(n - 32)), end='')
        else:
            print("{:c}".format(c), end='')
    print()
