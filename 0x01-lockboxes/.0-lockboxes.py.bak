#!/usr/bin/python3
"""
Determines if all the boxes can be opened
"""



def canUnlockAll(boxes):
    """
    Takes a list of lists (boxes) and determines if all can be opened

    """


    keys = {0}
    unlocked = {0}

    while True:
        new_keys = set()
        for box_idx in unlocked:
            for key in boxes[box_idx]:
                new_keys.add(key)

        if not new_keys:
            break

        keys.update(new_keys)
        unlocked.update(new_keys)

    return len(unlocked) == len(boxes)
