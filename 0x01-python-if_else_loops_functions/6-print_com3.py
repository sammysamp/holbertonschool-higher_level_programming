#!/usr/bin/python3
for d in range(0, 10):
    for u in range(0, 10):
        if d < u and d + u != 17:
            print("{}{}, ".format(d, u), end='')
        elif d == 8 and u == 9:
            print("{}{}".format(d, u))
