#!/usr/bin/python3
"""
Determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Takes a list of lists (boxes) and determines if all can be opened

    """

    keys = [0]

    for key in keys:
        for new_key in boxes[key]:
            if new_key not in keys and key < len(boxes):
                keys.append(new_key)

    print(keys)
    return len(keys) == len(boxes)
