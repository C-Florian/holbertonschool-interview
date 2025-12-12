#!/usr/bin/python3
"""
Lockboxes module
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of lists): list of boxes containing keys

    Returns:
        bool: True if all boxes can be opened, else False
    """
    if not isinstance(boxes, list):
        return False

    n = len(boxes)
    opened = [False] * n
    opened[0] = True

    keys = set(boxes[0])

    for key in keys:
        if 0 <= key < n and not opened[key]:
            opened[key] = True
            keys.update(boxes[key])

    return all(opened)
