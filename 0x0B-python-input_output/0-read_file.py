#!/usr/bin/python3
""" Reading a text file """

def read_file(filename=""):
    """read file method"""
    with open('my_file_0.txt', encoding='utf-8') as f:
        read_data = f.read()
    print(read_data)
