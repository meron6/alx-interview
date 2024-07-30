#!/usr/bin/python3
def canUnlockAll(boxes):
    # Initialize the list to track visited boxes
    n = len(boxes)
    visited = [False] * n
    visited[0] = True  # The first box is unlocked

    # Stack for DFS
    stack = [0]

    # Perform DFS
    while stack:
        box = stack.pop()

        for key in boxes[box]:
            if key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    # Check if all boxes are visited
    return all(visited)
