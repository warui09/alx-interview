#!/usr/bin/python3
"""check if provided data is valid utf-8"""


def validUTF8(data):
    """check if data is valid utf-8"""

    count = 0

    for i in range(len(data)):
        if count == 0:
            if data[i] >> 5 == 0b110:
                count = 1
            elif data[i] >> 4 == 0b1110:
                count = 2
            elif data[i] >> 3 == 0b11110:
                count = 3
            elif data[i] >> 7 != 0:
                return False
        else:
            if data[i] >> 6 != 0b10:
                return False
            count -= 1

    return count == 0
