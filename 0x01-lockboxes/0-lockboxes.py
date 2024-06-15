#!/usr/bin/python3
"""Module for Lockboxes question"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    n = len(boxes)
    unlocked = set()
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        if current_box not in unlocked:
            unlocked.add(current_box)
            for key in boxes[current_box]:
                if key < n and key not in unlocked:
                    queue.append(key)

    return len(unlocked) == n
