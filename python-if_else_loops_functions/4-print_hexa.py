#!/usr/bin/python3
print("".join(
    ["{} = 0x{}\n".format(i, hex(i)[2:]) for i in range(99)]
), end="")
