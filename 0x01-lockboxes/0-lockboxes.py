#!/usr/bin/python3
"""contains canUnlockAll function"""


def canUnlockAll(boxes):
    """Determines if all boxes in a given array of boxes can be opened

    Args:
        boxes(list of lists): the list at each index
        contains list of keys of boxes

    Return: True if all boxes can be opened, else return False
    """
    keys = [0]
    for key in keys:
        try:
            for new_key in boxes[key]:
                if new_key not in keys:
                    keys.append(new_key)
            boxes[key] = -1
        except IndexError:
            pass

    for box in boxes:
        if box != -1:
            return False
    return True
