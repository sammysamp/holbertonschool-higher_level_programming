#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cl = my_list.copy()
    for i in range(len(cl)):
        if cl[i] == search:
            cl[i] = replace
    return cl
