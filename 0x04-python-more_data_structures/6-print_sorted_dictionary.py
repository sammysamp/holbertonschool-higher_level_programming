#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    asort = sorted(a_dictionary)
    for s in asort:
        print(s + ": " + str(a_dictionary.get(s)))
    asort.clear()
