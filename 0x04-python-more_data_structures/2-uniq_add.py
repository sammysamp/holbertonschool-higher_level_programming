#!/usr/bin/python3
def uniq_add(my_list=[]):
    ltemp = []
    add = 0
    for i in my_list:
        if not(i in ltemp):
            add += i
        ltemp.append(i)
    ltemp.clear()
    return add
