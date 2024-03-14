#!/usr/bin/python3
"""
Determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Takes a list of lists (boxes) and determines if all can be opened

    """

    unlocked = False
    keys = []
    last_unlocked = 0

    for idx, box in enumerate(boxes):
        if idx == 0:
            unlocked = True
        elif idx in keys:
            last_unlocked = idx
            unlocked = True

        if not unlocked:
            break
        else:
            for key in box:
                keys.append(key)

    return last_unlocked == len(boxes) - 1
