#!/usr/bin/python3
"""
Contains the read_file module
"""

def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open('workfile', encoding="utf-8") as f:
        read_data = f.read()
        print(f.read(), end="")
