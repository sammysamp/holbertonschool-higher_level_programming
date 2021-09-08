#!/usr/bin/python3
def uppercase(str):
    for c in str:
        n = ord(c)
        if n > 96 and n < 123:
            plus = -32
        else:
            plus = 0
        print("{:c}".format(ord(c) + plus), end='')
    print()
