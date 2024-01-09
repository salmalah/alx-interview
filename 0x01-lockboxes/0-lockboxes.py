#!/usr/bin/python3
"""
open boxes
"""


def canUnlockAll(boxes):
    """
    This is a   method that determines
    if all the boxes can be opened
    """
    if not boxes or not boxes[0]:
        return False

    n = len(boxes)
    visited = set()
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        visited.add(current_box)

        for key in boxes[current_box]:
            if key < n and key not in visited:
                queue.append(key)

    return len(visited) == n
