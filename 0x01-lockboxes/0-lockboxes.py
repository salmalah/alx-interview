#!/usr/bin/python3
"""
this module is open boxes
"""


def canUnlockAll(boxes):
    """
    This is a  method that determines if all the boxes can be opened
    """
    box_s = set(boxes[0])
    for f in boxes[0]:
        if f < len(boxes):
            box_s.update(boxes[f])

    for e in range(1, len(boxes)):
        if e in box_s:
            box_s.update(boxes[e])
        else:
            return False

    return True
