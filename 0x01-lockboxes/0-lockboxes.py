#!/usr/bin/python3
"""
#boxes is a list of lists
#A key with same number as a box opens that box
#You can assume all keys will be positive integers
#There can be keys that do not have boxes
#The first box boxes[0] is unlocked
#Return True if all boxes can be opened, else return False.
"""
from collections import deque


def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = deque([0])

    while queue:
        current_box = queue.popleft()
        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
