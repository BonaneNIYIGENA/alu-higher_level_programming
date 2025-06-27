#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            # Convert lowercase to uppercase by subtracting 32
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))
