#!/usr/bin/python3
"""
Lockboxes module
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (list of lists): list of boxes containing keys

    Returns:
        bool: True if all boxes can be opened, else False
    """
    n = len(boxes)
    if n == 0:
        return True

    opened = [False] * n
    opened[0] = True

    stack = [0]

    while stack:
        box = stack.pop()

        for key in boxes[box]:
            if 0 <= key < n and not opened[key]:
                opened[key] = True
                stack.append(key)

    return all(opened)