#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
        language that combines remarkable power with very clear syntax"
str = str[39:66] + str[(38 + 68):(44 + 68)] + str[:6]
print(str)
