#!/usr/bin/python3
"""method"""


def write_file(filename="", text=""):
    """write on file create the file if doesn’t exist
    overwrite the content of the file if it already exists"""
    with open(filename, mode='w', encoding='UTF-8') as f:
        counter = f.write(text)
    return(counter)
