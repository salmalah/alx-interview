#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    :param boxes: A list of lists representing boxes and their keys.
    :return: True if all boxes can be opened, False otherwise.
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
